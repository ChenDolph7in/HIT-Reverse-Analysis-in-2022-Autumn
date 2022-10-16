# -*-coding:utf-8-*-
import sys
import struct

class PeParser:

    def __init__(self, file_path):
        self.MZSIG = b'MZ'
        self.PESIG = b'PE\0\0'
        self.path = file_path

    # 将十六进制数据转换为小端格式的数值
    def get_dword(self, data):
        return struct.unpack('<L', data)[0]

    # 提取ASCII字符串
    def get_string(self, ptr):
        beg = ptr
        while ptr < len(self.data) and self.data[ptr] != 0:
            ptr += 1
        return self.data[beg:ptr]

    def parse(self):
        self.read_data()
        if not self.is_valid_pe():
            print("[Error] Invalid PE file")
        self.parse_import_table()

    # 读取文件数据
    def read_data(self):
        fd = open(self.path, "rb")
        self.data = fd.read()
        fd.close()

    # 检查文件合法性并读取数据
    def is_valid_pe(self):
        e_magic = self.data[0:2]

        if e_magic != self.MZSIG:
            return False
        else:
            e_lfanew = self.get_dword(self.data[60:64])
            Machine = self.data[e_lfanew:e_lfanew + 4]

            if Machine != self.PESIG:
                return False
            else:
                return True

    # RVA转偏移地址
    def rva_to_offset(self, rva):
        # 取PE头地址RVA
        PE_header_RVA = self.get_dword(self.data[60:64])
        # 取可选头大小，用于跳过可选头找到节表
        SizeOfOptionalHeader = self.get_dword(self.data[PE_header_RVA + 0x14:PE_header_RVA + 0x14 + 2] + b"\x00\x00")
        IMAGE_SECTION_HEADER = PE_header_RVA + SizeOfOptionalHeader + 0x18
        NumberOfSections = self.get_dword(self.data[PE_header_RVA + 2:PE_header_RVA + 4] + b"\x00\x00")

        # section_ptr用于遍历所有节，找到RVA位于哪个节
        section_ptr = IMAGE_SECTION_HEADER
        for i in range(NumberOfSections + 1):
            # 若RVA位于当前节内  FOA = PointerToRawData + (VRA- VirtualAddress)
            if rva <= self.get_dword(self.data[section_ptr + 0x10:section_ptr + 0x14]) + self.get_dword(
                    self.data[section_ptr + 0xC: section_ptr + 0x10]) and rva >= self.get_dword(
                self.data[section_ptr + 0xc:section_ptr + 0x10]):
                return rva + self.get_dword(self.data[section_ptr + 0x14:section_ptr + 0x18]) - self.get_dword(
                    self.data[section_ptr + 0xc:section_ptr + 0x10])
            section_ptr = section_ptr + 0x28
        return 0

    # 输入表结构解析
    def parse_import_table(self):

        PE_header_RVA = self.get_dword(self.data[60:64])
        import_descriper_RVA = self.get_dword(self.data[PE_header_RVA + 0x80:PE_header_RVA + 0x80 + 4])
        IID_list_ptr = self.rva_to_offset(import_descriper_RVA)

        import_size = self.get_dword(self.data[PE_header_RVA + 0x80 + 4:PE_header_RVA + 0x80 + 8])
        print("RVA:0x%x" % import_descriper_RVA + "\t" + str(import_descriper_RVA))
        print("Size:0x%x" % import_size + "\t" + str(import_size))

        IID_list = []  # 用于保存IID
        # 遍历直到IID 对应 INT_list == 0
        while True:
            IID_struct = []  # IID数组结构: [DDL_name,INT_RVA]

            # 处理 name
            name_RVA = self.get_dword(self.data[IID_list_ptr + 12:IID_list_ptr + 16])
            name_str = self.rva_to_offset(name_RVA)
            name = self.get_string(name_str)
            IID_struct.append(name)

            # 处理INT RVA
            INT_list = self.get_dword(self.data[IID_list_ptr:IID_list_ptr + 4])

            if INT_list == 0:
                break

            IID_struct.append(INT_list)
            # 添加入IID LIST
            IID_list.append(IID_struct)
            IID_list_ptr += 20

        # 遍历解析每个IID的INT数组
        for i in range(len(IID_list)):
            print((str(IID_list[i][0], encoding='UTF-8')))
            self.parse_iid_int(IID_list[i][1])

    #	解析每个IID对应的IMAGE_THUNK_DATA类型的INT数组
    def parse_iid_int(self, ptr):
        INT = self.rva_to_offset(ptr)
        while True:
            INT_name = self.get_dword(self.data[INT: INT + 4])
            if INT_name == 0:
                break
            print("\t" + str(self.get_string(self.rva_to_offset(INT_name) + 2), encoding='UTF-8'))
            INT += 4


if __name__ == "__main__":
    if len(sys.argv) == 2:
        p = PeParser(sys.argv[1])
        p.parse()
