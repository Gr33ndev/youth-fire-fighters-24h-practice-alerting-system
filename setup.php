<?php
    $numberOfOperations = $_GET['numberOfOperations'] ?? 0;
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Setup</title>
</head>
<body>

<h1>Setup Einsätze</h1>

<?php
    if($numberOfOperations == 0 && empty($_POST)) {
?>
    <form action="setup.php" method="get">
        <label for="numberOfOperations">Einsatzanzahl</label>
        <input type="number" id="numberOfOperations" name="numberOfOperations"><br>
        <input type="submit" name="submit" value="Submit">
    </form>
<?php
    }
?>

<?php
if($numberOfOperations != 0 && empty($_POST)){
?>
<form action="setup.php" method="POST">

<?php
    for($i = 0; $i < $numberOfOperations; $i++) {
?>
        <p>-------------------------</p>
        <p>| Einsatznummer <?php echo $i+1; ?> |</p>
        <p>-------------------------</p>

        <input name="numberOfOperations" value="<?php echo $numberOfOperations; ?>" hidden>
        <input name="operationNumber<?php echo "-" . $i . 1; ?>" value="<?php echo $i+1; ?>" hidden>
        <label for="operationDescription">Einsatzbeschreibung</label>
        <input type="text" id="operationDescription" name="operationDescription<?php echo "-" . $i . 1; ?>"><br>
        <label for="address">Adresse</label>
        <input type="text" id="address" name="address<?php echo "-" . $i . 1; ?>"><br>
        <label for="operationDate">Einsatzdatum</label>
        <input type="date" id="operationDate" name="operationDate<?php echo "-" . $i . 1; ?>"><br>
        <label for="operationTime">Einsatzuhrzeit</label>
        <input type="time" id="operationTime" name="operationTime<?php echo "-" . $i . 1; ?>"><br>

        <label for="1/19">1/19</label>
        <input type="checkbox" id="1/19" name="1/19<?php echo "-" . $i . 1; ?>"><br>
        <label for="1/42">1/42</label>
        <input type="checkbox" id="1/42" name="1/42<?php echo "-" . $i . 1; ?>"><br>
        <label for="2/42">2/42</label>
        <input type="checkbox" id="2/42" name="2/42<?php echo "-" . $i . 1; ?>"><br>
        <label for="3/48">3/48</label>
        <input type="checkbox" id="3/48" name="3/48<?php echo "-" . $i . 1; ?>"><br>

        <label for="oil">Öl</label>
        <input type="checkbox" id="oil" name="oil<?php echo "-" . $i . 1; ?>"><br>
        <label for="hoseCart">SW</label>
        <input type="checkbox" id="hoseCart" name="hoseCart<?php echo "-" . $i . 1; ?>"><br>
        <label for="drk">DRK</label>
        <input type="checkbox" id="drk" name="drk<?php echo "-" . $i . 1; ?>"><br>
        <label for="police">POL</label>
        <input type="checkbox" id="police" name="police<?php echo "-" . $i . 1; ?>"><br>

<?php
    }
?>
    <input type="submit" value="Submit">
</form>
<?php
}
?>



<?php
if(!empty($_POST)){

    $json = "[";

    for($i = 0; $i < $_POST['numberOfOperations']; $i++){
        $postArray = array(
            "operationNumber" => $_POST['operationNumber' . "-" . $i . 1],
            "operationDescription" => $_POST['operationDescription' . "-" . $i . 1],
            "address" => $_POST['address' . "-" . $i . 1],
            "operationDate" => $_POST['operationDate' . "-" . $i . 1],
            "operationTime"  => $_POST['operationTime' . "-" . $i . 1],

            "1-19"  => $_POST['1/19' . "-" . $i . 1] ?? "off",
            "1-42"  => $_POST['1/42' . "-" . $i . 1] ?? "off",
            "2-42"  => $_POST['2/42' . "-" . $i . 1] ?? "off",
            "3-48" => $_POST['3/48' . "-" . $i . 1] ?? "off",

            "oil" => $_POST['oil' . "-" . $i . 1] ?? "off",
            "hoseCart" => $_POST['hoseCart' . "-" . $i . 1] ?? "off",
            "drk" => $_POST['drk' . "-" . $i . 1] ?? "off",
            "police" => $_POST['police' . "-" . $i . 1] ?? "off"
        );

        $json .= json_encode($postArray);

        if($_POST['numberOfOperations'] > $i+1){
            $json .= ",";
        }

        if($_POST['numberOfOperations'] == $i+1){
            $json .= "]";
        }

        $file = 'config.json';
    }

    if(isset($file)){
        file_put_contents( $file, $json);
    }
}
?>
<?php
    if(!empty($_POST)){
?>
        <h3>Setup erfolgreich abgeschlossen</h3>
<?php
    }
?>
</body>
</html>