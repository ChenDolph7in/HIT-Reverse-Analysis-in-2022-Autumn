<?php
function encode($D,$K){
    for($i=0;$i<strlen($D);$i++){
        $c = $K[$i+1&15];
        $D[$i] = $D[$i]^$c;
    }
    return $D;
}

$pass='pass';
$payloadName='payload';
$key='3c6e0b8a9c15224a';
// 原来的数据去掉前十六位和后十六位然后解密
echo base64_decode(encode(base64_decode('NGaGBQWDEHPw'),$key));

?>