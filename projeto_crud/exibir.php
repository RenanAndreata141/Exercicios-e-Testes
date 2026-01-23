<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="Stylesheet" type="text/css" href="estilo.css">
    </head>
    <body>
        <section id="formcad">
            <form method="GET" action="#">
                Nome: <input type="text" name="nome">
                <br>
                Componente: <input type="text" name="componente">
                <br>
                Nota 1: <input type="number" name="nota1">
                <br>
                Nota 2: <input type="number" name="nota2">
                <br>
                Nota 3: <input type="number" name="nota3">
                <br>
                Nota 4: <input type="number" name="nota4">

                <input type="submit" name="enviar" value="Cadastrar" id="cadastrar" id="btncad">
            </form>
        </section>
        <br>
        <section id="tbl">
            <table border="10px">
                <section id="tit">
                    <thead>
                        <th> Id </th>
                        <th> Nome </th>
                        <th> Componente </th>
                        <th> 1° Bimestre </th>
                        <th> 2° Bimestre </th>
                        <th> 3° Bimestre</th>
                        <th> 4° Bimestre </th> 
                        <th> 
                            <form method="GET" action="#">
                                <input type="search" name="pesquisa" placeholder="Pesquisa">
                            </form>
                        </th>
                    </thead><br>        
                </section>
                <section id="linha">

                    <?php
                        include('cnx.php'); 

                        if(isset($_GET['enviar'])){
                            $nome = $_GET['nome'];
                            $componente = $_GET['componente'];
                            $nota1 = $_GET['nota1'];
                            $nota2 = $_GET['nota2'];
                            $nota3 = $_GET['nota3'];
                            $nota4 = $_GET['nota4'];

                            $sql1 = 'insert into notas (nome, componentes, pribim, segbim, terbim, quarbim) values ("'.$nome.'","'.$componente.'",'.$nota1.','.$nota2.','.$nota3.','.$nota4.');';
                            mysqli_query($conexao, $sql1);
                                    
                                
                            header('location:exibir.php');
                        }
                        $sql = 'select * from notas;';

                        if(isset($_GET['pesquisa'])){
                            $pes = $_GET['pesquisa'];

                            $sql = "SELECT * FROM notas WHERE nome LIKE '%".$pes."%'";
                        }

                        $resul = mysqli_query($conexao, $sql);

                        while($con = mysqli_fetch_array($resul)){
                            echo '<tr id="linha"><td>' . $con['id'].'</td><td>' . $con['nome'].'</td><td>'.$con['componentes'].'</td><td>'.$con['pribim'].'</td><td>'.$con['segbim'].'</td><td>'.$con['terbim'].'</td><td>'.$con['quarbim'].'</td>
                            <td id="apaga"><a href="exibir.php?ex='.$con['id'].'"><img id="icone" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAmcxBRIFxVwd6qppn576MWFblCTHEPlJxFplnCsuVRg&s"></a></td>
                            
                            <td id="edita"><a href="exibir.php?ed='.$con['id'].'"><img id="icone" src="https://cdn-icons-png.flaticon.com/512/181/181672.png"></a></td>
                            </tr>
                            <br>';
                        }
                        
                        if(isset($_GET['ex'])){
                            $ex = $_GET['ex'];

                            $sql2 = "DELETE FROM notas WHERE id = '".$ex."';";
                            mysqli_query($conexao, $sql2);
                            header("location:exibir.php");
                        }

                        if(isset($_GET['ed'])){
                            $ed = $_GET['ed'];

                            $sqlpes = 'select * from notas where id = '.$ed;
                            $resul = mysqli_query($conexao,$sqlpes);

                            $con = mysqli_fetch_array($resul);

                        ?>
                            <form method="POST" action="#">
                                Nome: <input type="text" name="nomeed" value="<?php echo $con['nome'];  ?>">
                                <br>
                                Componente: <input type="text" name="componenteed" value="<?php echo $con['componentes'];  ?>">
                                <br>
                                Nota 1: <input type="number" name="nota1ed" value="<?php echo $con['pribim'];  ?>">
                                <br>
                                Nota 2: <input type="number" name="nota2ed" value="<?php echo $con['segbim'];  ?>">
                                <br>
                                Nota 3: <input type="number" name="nota3ed" value="<?php echo $con['terbim'];  ?>">
                                <br>
                                Nota 4: <input type="number" name="nota4ed" value="<?php echo $con['quarbim'];  ?>">
                                <input type="submit" name="confirmar" value="Confirmar" id="confirmar">
                            </form>
                        <?php
                            
                        }
                
                        if(isset($_POST['confirmar'])){
                            $ed = $_GET['ed'];
                            $nomeed = $_POST['nomeed'];
                            $componenteed = $_POST['componenteed'];
                            $nota1ed = $_POST['nota1ed'];
                            $nota2ed = $_POST['nota2ed'];
                            $nota3ed = $_POST['nota3ed'];
                            $nota4ed = $_POST['nota4ed'];
                            $sqled=('update notas set nome="'. $nomeed .'", componentes="'.$componenteed .'", pribim="'.$nota1ed .'", segbim="'.$nota2ed .'", terbim="'.$nota3ed .'", quarbim="'.$nota4ed .'" where id='.$ed);
                            mysqli_query($conexao, $sqled);
                            header("location:exibir.php");
                        }


                        ?>
                </section>
            </table>
        </section>
    </body>
</html>
