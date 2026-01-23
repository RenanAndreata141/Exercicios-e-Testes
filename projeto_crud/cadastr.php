<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="Stylesheet" href="style.css">
    <title>Cadastrar</title>
</head>
<body>
    <section id="login">
        <h1>Cadastro</h1>
        <form method="POST" action="#">
            <p><input type="text" name="usuario"></p>
            <p><input type="password" name="senha"></p>
            <p><input type="submit" name="enviar" value="Cadastro" id="btnlogin"></p>
        </form>
        <a href="login.php">Não possui cadastro?</a>
    </section>

    <?php
        require_once('cnx.php');

        if(isset($_POST['enviar'])){
            $usuario= $_POST['usuario'];
            $senha= $_POST['senha'];

            $sql= 'INSERT INTO usuarios (usuarios, senha) VALUES ("'.$usuario.'","'.$senha.'");';
            mysqli_query($conexao, $sql);
        }
    ?>

</body>
</html>