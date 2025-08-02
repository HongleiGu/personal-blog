
so we go to
https://jupiter.challenges.picoctf.org/problem/60915/8028f.html

we have

```    Guess you found the robots
    picoCTF{ca1cu1at1ng_Mach1n3s_8028f}
```
basically the robots.txt is for web crawlers, telling which page they
should access, which they should not

## practise: picoctf vault-door-training

Your mission is to enter Dr. Evil\'s laboratory and retrieve the
blueprints for his Doomsday Project. The laboratory is protected by a
series of locked vault doors. Each door is controlled by a computer and
requires a password to open. Unfortunately, our undercover agents have
not been able to obtain the secret passwords for the vault doors, but
one of our junior agents obtained the source code for each vault\'s
computer! You will need to read the source code for each level to figure
out what the password is for that vault door. As a warmup, we have
created a replica vault in our training facility. The source code for
the training vault is here: VaultDoorTraining.java

```    import java.util.*;

    class VaultDoorTraining {
        public static void main(String args[]) {
            VaultDoorTraining vaultDoor = new VaultDoorTraining();
            Scanner scanner = new Scanner(System.in); 
            System.out.print("Enter vault password: ");
            String userInput = scanner.next();
        String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
        if (vaultDoor.checkPassword(input)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
       }

        // The password is below. Is it safe to put the password in the source code?
        // What if somebody stole our source code? Then they would know what our
        // password is. Hmm... I will think of some ways to improve the security
        // on the other doors.
        //
        // -Minion #9567
        public boolean checkPassword(String password) {
            return password.equals("w4rm1ng_Up_w1tH_jAv4_be8d9806f18");
        }
    }
```
so it is just hard-coded

the flag is picoCTF{w4rm1ng_Up_w1tH_jAv4_be8d9806f18}

## practise picoctf format_string0

Can you use your knowledge of format strings to make the customers
happy? Download the binary here. Download the source here. Additional
details will be available after launching your challenge instance.

```    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #include <signal.h>
    #include <unistd.h>
    #include <sys/types.h>

    #define BUFSIZE 32
    #define FLAGSIZE 64

    char flag[FLAGSIZE];

    void sigsegv_handler(int sig) {
        printf("\n%s\n", flag);
        fflush(stdout);
        exit(1);
    }

    int on_menu(char *burger, char *menu[], int count) {
        for (int i = 0; i < count; i++) {
            if (strcmp(burger, menu[i]) == 0)
                return 1;
        }
        return 0;
    }

    void serve_patrick();

    void serve_bob();


    int main(int argc, char **argv){
        FILE *f = fopen("flag.txt", "r");
        if (f == NULL) {
            printf("%s %s", "Please create 'flag.txt' in this directory with your",
                            "own debugging flag.\n");
            exit(0);
        }

        fgets(flag, FLAGSIZE, f);
        signal(SIGSEGV, sigsegv_handler);

        gid_t gid = getegid();
        setresgid(gid, gid, gid);

        serve_patrick();

        return 0;
    }

    void serve_patrick() {
        printf("%s %s\n%s\n%s %s\n%s",
                "Welcome to our newly-opened burger place Pico 'n Patty!",
                "Can you help the picky customers find their favorite burger?",
                "Here comes the first customer Patrick who wants a giant bite.",
                "Please choose from the following burgers:",
                "Breakf@st_Burger, Gr%114d_Cheese, Bac0n_D3luxe",
                "Enter your recommendation: ");
        fflush(stdout);

        char choice1[BUFSIZE];
        scanf("%s", choice1);
        char *menu1[3] = {"Breakf@st_Burger", "Gr%114d_Cheese", "Bac0n_D3luxe"};
        if (!on_menu(choice1, menu1, 3)) {
            printf("%s", "There is no such burger yet!\n");
            fflush(stdout);
        } else {
            int count = printf(choice1);
            if (count > 2 * BUFSIZE) {
                serve_bob();
            } else {
                printf("%s\n%s\n",
                        "Patrick is still hungry!",
                        "Try to serve him something of larger size!");
                fflush(stdout);
            }
        }
    }

    void serve_bob() {
        printf("\n%s %s\n%s %s\n%s %s\n%s",
                "Good job! Patrick is happy!",
                "Now can you serve the second customer?",
                "Sponge Bob wants something outrageous that would break the shop",
                "(better be served quick before the shop owner kicks you out!)",
                "Please choose from the following burgers:",
                "Pe%to_Portobello, $outhwest_Burger, Cla%sic_Che%s%steak",
                "Enter your recommendation: ");
        fflush(stdout);

        char choice2[BUFSIZE];
        scanf("%s", choice2);
        char *menu2[3] = {"Pe%to_Portobello", "$outhwest_Burger", "Cla%sic_Che%s%steak"};
        if (!on_menu(choice2, menu2, 3)) {
            printf("%s", "There is no such burger yet!\n");
            fflush(stdout);
        } else {
            printf(choice2);
            fflush(stdout);
        }
    }
```
just run the binary excutable and try out every option, the flag will
bump out after the correct combination is found

picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_74f6c0e7}

# web

##
:::::::
:::::::::::::::::
::::::::::::::::::
