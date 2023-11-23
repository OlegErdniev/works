<header class="header">
    <div class="container">
        <div class="header__inner">
            <div class="header__logo">
                <img class="img_logo" src="img/main_logo.png" alt="">
            </div>
            <nav class="nav">
                <a class="nav__link" href="верстка1.html">Main</a>
                <a class="nav__link" href="Features.html">Features</a>
                <a class="nav__link" href="#">Our Team</a>
                <a class="nav__link" href="#">Testimonials</a>
                <a class="nav__link" href="register.html">Log in</a>
            </nav>
        </div>
    </div>
</header>
<div class="intro">
    <div class="container">
        <div class="intro__inner">
            <div class="container mt-4">
                
                <h1>Registration form</h1>
                <form action="check.php" method="post">
                    <input type="text" class="form-control" name="login"
                    id ="login" placeholder="Your login"><br>
                    <input type="text" class="form-control" name="name"
                    id ="name" placeholder="Your name"><br>
                    <input type="password" class="form-control" name="pass"
                    id ="pass" placeholder="Your password"><br>
                    <button class="btn btn-success" type="submit">Register</button>

                </form>
            </div>
            <div class="container mt-4">
                <h1>Log in form</h1>
                <form action="auth.php" method="post">
                    <input type="text" class="form-control" name="login1"
                    id ="login1" placeholder="Your login"><br>
                    
                    <input type="password" class="form-control" name="pass1"
                    id ="pass1" placeholder="Your password"><br>
                    <button class="btn btn-success" type="submit">Log in</button>

                </form>
            </div>
            
        </div>
    </div>
</div>