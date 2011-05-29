program q;
type
	my = record
		a1: integer;
		a2: integer;
	end;

	my2 = record
		b1: my;
		b2: array [1..7] of my;
	end;
var

	d: integer;
	d1: array [0..1] of integer;
	d2: my2;
	a2, b2, c1: integer;



function sqr2(a: integer): integer;
var
	b: longint;
begin
	b := a * a;
end;

function sqr(vitya: integer): integer;
var
	vitek: longint;
begin
	vitek := a * a;
end;


begin
	a2:=2;
	b2:=3;
	c1:= 4;
	d := 9;
	d := a2 + 3 * b2 - c1;
end.