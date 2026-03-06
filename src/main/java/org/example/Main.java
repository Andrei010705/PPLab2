package org.example;

import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Source;
import org.graalvm.polyglot.Value;

import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Scanner;

public class Main {

    private static final String BASE_PATH = "src/main/java/org/example/";

    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Alege o optiune:");
        System.out.println("1. Ruleaza prime_numbers.js");
        System.out.println("2. Ruleaza prime_numbers.py");
        System.out.println("3. Ruleaza generate_list.py");
        System.out.println("4. Ruleaza generate_list.py + show_list.js + sort_list.py");
        System.out.println("5. Ruleaza linear_regression.py");
        System.out.print("Optiunea ta: ");

        int option = scanner.nextInt();

        switch (option) {
            case 1:
                runJavaScript("prime_numbers.js");
                break;
            case 2:
                runPython("prime_numbers.py");
                break;
            case 3:
                runPython("generate_list.py");
                break;
            case 4:
                runPythonAndJavaScript("generate_list.py", "show_list.js", "sort_list.py");
                break;
            case 5:
                runPython("linear_regression.py");
                break;
            default:
                System.out.println("Optiune invalida.");
        }

        scanner.close();
    }

    private static void runJavaScript(String fileName) throws Exception {
        System.out.println("Executam JavaScript: " + fileName);

        String code = readFile(fileName);

        try (Context context = Context.newBuilder("js")
                .allowAllAccess(true)
                .build()) {

            context.eval(Source.newBuilder("js", code, fileName).build());
        }
    }

    private static void runPython(String fileName) throws Exception {
        System.out.println("Executam Python: " + fileName);

        String code = readFile(fileName);

        try (Context context = Context.newBuilder("python")
                .allowAllAccess(true)
                .build()) {

            context.eval(Source.newBuilder("python", code, fileName).build());
        }
    }

    private static void runPythonAndJavaScript(String pythonFile, String jsFile, String sortPythonFile) throws Exception {
        System.out.println("Executam fisiere combinate: " + pythonFile + ", " + jsFile + ", " + sortPythonFile);

        String pythonCode = readFile(pythonFile);
        String jsCode = readFile(jsFile);
        String sortPythonCode = readFile(sortPythonFile);

        try (Context context = Context.newBuilder()
                .allowAllAccess(true)
                .build()) {

            context.eval(Source.newBuilder("python", pythonCode, pythonFile).build());

            Value pythonBindings = context.getBindings("python");
            Value lista = pythonBindings.getMember("lista");

            context.getBindings("js").putMember("lista", lista);
            context.eval("js", jsCode);

            context.getBindings("python").putMember("lista", lista);
            context.eval("python", sortPythonCode);
        }
    }

    private static String readFile(String fileName) throws Exception {
        return Files.readString(Path.of(BASE_PATH + fileName));
    }
}