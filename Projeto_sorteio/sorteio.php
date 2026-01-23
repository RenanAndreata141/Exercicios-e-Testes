<?php
session_start();

if (!isset($_SESSION['pessoas'])) {
    $_SESSION['pessoas'] = ["Ana", "Bruno", "Carla", "Daniel", "Eduardo", "Fernanda", "Gustavo", "Helena", "Renan"];
}

if (isset($_POST['adicionar'])) {
    $novos_nomes = explode(",", $_POST['novas_pessoas']);
    $novos_nomes = array_map('trim', $novos_nomes);
    
    $_SESSION['pessoas'] = array_merge($_SESSION['pessoas'], $novos_nomes);
    echo "<p style='color: green;'>Pessoas adicionadas com sucesso!</p>";
}

$pessoas = &$_SESSION['pessoas'];

$mensagem_sorteio = "";
if (isset($_POST['sortear'])) {
    if (empty($pessoas)) {
        $mensagem_sorteio = "Não há mais pessoas para sortear. Adicione mais abaixo!";
    } else {
        $indice_sorteado = array_rand($pessoas);
        $nome_sorteado = $pessoas[$indice_sorteado];
        $mensagem_sorteio = "Pessoa sorteada: <strong>$nome_sorteado</strong>";
    
        unset($pessoas[$indice_sorteado]);
        $_SESSION['pessoas'] = array_values($pessoas); 
    }
}
?>

<!DOCTYPE html>
<html lang="pt_br">
<head>
    <meta charset="UTF-8">
    <title>Sorteio de Pessoas</title>
</head>
<body>
    <h1>Sorteio de Pessoas</h1>
    
    <?php if ($mensagem_sorteio): ?>
        <p><?php echo $mensagem_sorteio; ?></p>
    <?php endif; ?>

    <form method="post">
        <button type="submit" name="sortear">Sortear Pessoa</button>
    </form>

    <hr>

    <h3>Adicionar Pessoas</h3>
    <form method="post">
        <label for="novas_pessoas">Nomes (separados por vírgula):</label><br>
        <input type="text" id="novas_pessoas" name="novas_pessoas" required>
        <button type="submit" name="adicionar">Adicionar</button>
    </form>
    
    <p>Pessoas restantes no pote: <?php echo count($_SESSION['pessoas']); ?></p>
</body>
</html>