# 2022年秋季学期逆向分析

## 实验一 Afkayas.1.Exe

* 第三步（1）中，使用bpx rtcMsgBox打断点并执行到断点后，需进行一次步入，否则栈顶不会出现返回地址
  * 调用者执行call指令，将下一条指令地址入栈（**push eip**）
  * 但执行到断点时，call执行未执行
* 第三步（2）中，“单步步过之后”，未必指“进行一次步过”