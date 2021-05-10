package week10;

public class Overs {
	public static void main(String[] args) {
		Parent p = new Parent();
		Child c = new Child();
		Parent h = new Child();
		p.parentMethod(); // p
		c.parentMethod(); // c
		h.parentMethod(); // c
	}
}

class Parent{
	void parentMethod() {
		System.out.println("called P");
	}
}

class Child extends Parent{
	void parentMethod() {System.out.println("called C");}     // 오버라이딩
	void parentMethod(int x) {} //오버로딩
	
	void childMethod() {}
	void childMethod(int a) {} //오버로딩
}
