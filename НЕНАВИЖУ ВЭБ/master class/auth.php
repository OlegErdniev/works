<?php
    $login = filter_var(trim($_POST['login1']), FILTER_SANITIZE_STRING);
    $pass = filter_var(trim($_POST['pass1']), FILTER_SANITIZE_STRING);
    
    //$pass = md5($pass."ghjsflkd2345")
    $mysql = new mysqli('localhost', 'root', 'root', 'register-bd111');
    $result = $mysql->query("SELECT * FROM `register-bd` WHERE `login` = '$login' AND `pass` = '$pass'")

    $user = $result->fetch_assoc();
    if(count($user) == 0){
        echo "User not find";
        exit();
    }
    
    //setcookie('user', $user['name'], time() + 1500, "/");

    //header('Location: /');
    
?>
