# 2022年秋季学期逆向分析

## 实验一 Afkayas.1.Exe

* 第三步（1）中，使用bpx rtcMsgBox打断点并执行到断点后，需进行一次步入，否则栈顶不会出现返回地址
  * 调用者执行call指令，将下一条指令地址入栈（**push eip**）
  * 但执行到断点时，call执行未执行
* 第三步（2）中，“单步步过之后”，未必指“进行一次步过”，**可能进行多次**



## 实验二 PE文件结构分析

参考课上PPT **软件加壳与脱壳.pdf** 内PE文件的结构图，对理解PE文件结构有很大帮助

注意**FOA，RVA，VirtualAddress，ImageBase，PointerToRawData，AddressOfEntryPoint**的关系