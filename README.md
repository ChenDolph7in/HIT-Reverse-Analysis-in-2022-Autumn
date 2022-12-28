# 2022年秋季学期逆向分析

1. <font color=red>注意</font>
   * vmware版本最好升级到最高版本***再导入***，确保vmx文件版本与vmware版本兼容；网站内下载vmware版本与win10不匹配，可能出现问题：
     * vmware版本与win10不兼容：传输文件时若文件大小过大则系统蓝屏
     * vmx文件版本与vmware版本不兼容：若干分钟wmware work station未响应
2. 其他
   * 使用方法：解压->vwmare内：文件->打开->找到解压文件夹内的vmx文件->确定

## 实验一 Afkayas.1.Exe

* 第三步（1）中，使用bpx rtcMsgBox打断点并执行到断点后，需进行一次步入，否则栈顶不会出现返回地址
  * 调用者执行call指令，将下一条指令地址入栈（**push eip**）
  * 但执行到断点时，call执行未执行
* 第三步（2）中，“单步步过之后”，未必指“进行一次步过”，**可能进行多次**



## 实验二 PE文件结构分析

参考课上PPT **软件加壳与脱壳.pdf** 内PE文件的结构图，对理解PE文件结构有很大帮助

注意**FOA，RVA，VirtualAddress，ImageBase，PointerToRawData，AddressOfEntryPoint**的关系



## 实验三 栈缓冲区溢出

* ”Hello “字符串后面有个空格

<font color = red>注意：</font>实验前备份虚拟机，否则攻击代码完成账户创建后会导致我们不知道账户密码而无法在下一次进入虚拟机时登录系统



## 实验四

二 1.（5）没有搞出来

1. 缺少可运行PHP的服务器环境
2. 下载PHPStudy尝试运行后发现不能只是通过php逆向backdoor.php中代码的过程，需要使用`urldecode()`初步处理，详见`decode.php`。就算如此，也只是成功解码出攻击者发往受害主机的指令，不知为何没有解出受害主机返回的信息。
3. PHPStudy服务器似乎有漏洞，导致本人第二天被盗号；加上时间紧迫，实在没有时间，故放弃进一步研究。

