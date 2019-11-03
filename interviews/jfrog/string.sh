a="Roopam"
b="Divya"
c=""
[ "$a" = "$b" ]
echo $?
[ -n "$a" ]
echo $?
[ -z "$c" ]
echo $?

var="Test String"
echo ${var:5:6}
