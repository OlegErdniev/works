<?php
    $login = filter_var(trim($_POST['login']), FILTER_SANITIZE_STRING);
    $name = filter_var(trim($_POST['name']), FILTER_SANITIZE_STRING);
    $pass = filter_var(trim($_POST['pass']), FILTER_SANITIZE_STRING);

    if (mb_strlen($login) < 5 || mb_strlen($login) >15){
        echo"Error: Incorrect lenght(5 to 15)";
        exit();
    }
    if (mb_strlen($name)<5 || mb_strlen($name) >20){
        echo"Error: Incorrect lenght(5 to 20)";
        exit();
    }
    if (mb_strlen($pass)<3 || mb_strlen($pass) > 20){
        echo"Error: Incorrect lenght(3 to 20)";
        exit();
    }
    $mysql = new mysqli('localhost', 'root', 'root', 'register-bd111');
    $mysql->query("INSERT INTO `register-bd` (`login`, `pass`, `name`)
    VALUES('$login', '$pass', '$name')");
    $mysql->close();
    header('Location: /');
    exit();


?>