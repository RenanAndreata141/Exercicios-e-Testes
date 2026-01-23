<!DOCTYPE html>
    <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title>Login</title>
            <link rel="Stylesheet" href="style.css">
        </head>
    <body>
        <section id="login">
            <h1> Login </h1>
            <form method="POST" action="#">
            <p><input type="text" name="usuario"></p>
            <p><input type="password" name="senha"></p>
                <input type="submit" name="login" value="Login" id="btnlogin">
            </form>
        <a href="cadastr.php">Não possui cadastro?</a>
        </section>

        <?php
            require_once('cnx.php');

            if(isset($_POST['login'])){
                $usuario = $_POST['usuario'];
                $senha = $_POST['senha'];

                $sql = 'INSERT INTO usuarios (usuario, senha) values ("'.$usuario.'",'.$senha.')';
                mysqli_query($conexao, $sql);
            }
        ?>
    </body>
</html>