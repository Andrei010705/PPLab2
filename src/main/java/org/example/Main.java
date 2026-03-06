package org.example;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Value;
import java.util.Set;
import org.graalvm.polyglot.Source;
import java.nio.file.Path;
import java.nio.file.Files;

public class Main {
    public static void main(String[] args) throws Exception {
//        Path jsPath = Path.of("src/main/java/org/example/primes.js");
//        String jsCode = Files.readString(jsPath);

//        Path pyPath = Path.of("src/main/java/org/example/primes.py");
//        String pyCode = Files.readString(pyPath);

        Path pyPath = Path.of("src/main/java/org/example/random.py");
        String pyCode = Files.readString(pyPath);


        Path jsPath = Path.of("src/main/java/org/example/showList.js");
        String jsCode = Files.readString(jsPath);

//        System.out.println("Asteptam executarea codului JavaScript");
//        try (Context context = Context.newBuilder("js").allowAllAccess(true).build()) {
//            context.eval(Source.newBuilder("js", jsCode, "primes.js").build());
//        }

//        System.out.println("Asteptam executarea codului Python... ");
//        try(Context context = Context.newBuilder("python").allowAllAccess(true).build() ) {
//            context.eval(Source.newBuilder("python", pyCode, "primes.py").build());
//        }

//        System.out.println("Asteptam executarea codului Python... ");
//        try(Context context = Context.newBuilder("python").allowAllAccess(true).build() ) {
//            context.eval(Source.newBuilder("python", pyCode, "random.py").build());
//        }



//        try(Context context = Context.newBuilder().allowAllAccess(true).build())
//        {
//            Value pyBindings = context.getBindings("python");
//            context.eval(Source.newBuilder("python", pyCode, "random.py").build());
//            Value lista = pyBindings.getMember("lista");
//
//            context.getBindings("js").putMember("lista", lista);
//            context.eval("js", jsCode);
//
//
//            context.getBindings("python").putMember("lista", lista);
//            String sortPy = Files.readString(Path.of("src/main/java/org/example/sortList.py"));
//            context.eval("python", sortPy);
//
//        }


//        try(Context context = Context.newBuilder().allowAllAccess(true).build()) {
//            context.eval(Source.newBuilder("python", Files.readString(Path.of("src/main/java/org/example/primes.py")), "primes.py").build());
//
//        }

        try (Context context = Context.newBuilder()
                .allowAllAccess(true)
                .build()) {

            context.eval(
                    Source.newBuilder(
                            "python",
                            Files.readString(
                                    Path.of("src/main/java/org/example/Ex2.py")),
                            "Ex2.py"
                    ).build()
            );
        }



    }
}