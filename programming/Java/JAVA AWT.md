This was done in class
THE CODE

package studentdetail;
import java.awt.*;
public class StudentDetail{
    StudentDetail(){
        Frame f = new Frame();
        Label name = new Label("Name");
        Label reg = new Label("RegNo");
        Label course = new Label("Course");
        Label year = new Label ("Year");
        Label semester = new Label("Semester");
        Button b = new Button("Submit");
        TextField t = new TextField();
        TextField t1 = new TextField();
        TextField t2 = new TextField();
        TextField t3 = new TextField();
        TextField t4 = new TextField();
        
        name.setBounds (20,80,80,30);
        reg.setBounds (20,150,80,30);
        course.setBounds (20,200,80,30);
        year.setBounds (20,250,80,30);
        semester.setBounds (20,300,80,30);
        
        t.setBounds(150,80,120,30);
        t1.setBounds(150,150,120,30);
        t2.setBounds(150,200,120,30);
        t3.setBounds(150,250,120,30);
        t4.setBounds(150,300,120,30);
        
        b.setBounds (100, 350,80,30);
        
        f.add(name);
        f.add(reg);
        f.add(course);
        f.add(year);
        f.add(semester);
        
        f.add(b);
        
        f.add(t);
        f.add(t1);
        f.add(t2);
        f.add(t3);
        f.add(t4);
        
        f.setSize(400,300);
        f.setTitle("Student detail");
        f.setLayout(null);
        f.setVisible(true);
      
    }
    public static void main(String []args){
        StudentDetail awt_obj = new StudentDetail();
    }
}


# Daily Learning Log — [02/11/2026]

## 1. What did I study today?

- using the java awt..
- Java can be used the same as visual basic studio to form an interaction.
- Keeping in mind that java is a language that is used in the internet...so this just make sense since it will form the interactions between the user and the program
- while using the "setBounds" The first number is the distance from the left side of the screen, the second input is the distance from the upper part of the screen.

## 2. What did I accomplish?

From the lectures the program above is what i accomplished

## 3. Practical work
The program above.

## 4. Screenshots
![[Pasted image 20261102144620.png]]
This is what the above code gave me
## 5. Challenges
setBounds....The first input is the distance from the right end of the line,,Then the second is the distance from the top

## 6. How I solved them

Changing the second number in the input section.

## 7. What I understand now

Explain what I can confidently teach someone else.

## 8. What I still need to improve

- The relationship between constructors and methods and calling out of objects...(There is something deeper in this. Not just calling an object from a class...)
- 

## 9. Tomorrow's target

1.Finish the stage 1 of the vault core 
2.Polish cybersecurity skills
3