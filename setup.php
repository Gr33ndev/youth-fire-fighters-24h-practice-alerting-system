<?php
error_reporting(E_ALL ^ E_NOTICE);

$numberOfOperations = $_GET['numberOfOperations'] ?? 0;

if (file_exists('config.json')) {
    $fromJson = json_decode(file_get_contents('config.json'), true);

    for ($i = 0; $i < $fromJson[0]['numberOfOperations']; $i++) {
        $operationDescription[$fromJson[$i + 1]['operationNumber']] = $fromJson[$i + 1]['operationDescription'] ?? "";
        $address[$fromJson[$i + 1]['operationNumber']] = $fromJson[$i + 1]['address'] ?? "";
        $operationDate[$fromJson[$i + 1]['operationNumber']] = $fromJson[$i + 1]['operationDate'] ?? "";
        $operationTime[$fromJson[$i + 1]['operationNumber']] = $fromJson[$i + 1]['operationTime'] ?? "";

        $oneNineteen[$fromJson[$i + 1]['operationNumber']] = $fromJson[$i + 1]['1-19'] ?? "";
        $oneFortyTwo[$fromJson[$i + 1]['operationNumber']] = $fromJson[$i + 1]['1-42'] ?? "";
        $twoFortyTwo[$fromJson[$i + 1]['operationNumber']] = $fromJson[$i + 1]['2-42'] ?? "";
        $threeFortyEight[$fromJson[$i + 1]['operationNumber']] = $fromJson[$i + 1]['3-48'] ?? "";

        $oil[$fromJson[$i + 1]['operationNumber']] = $fromJson[$i + 1]['oil'] ?? "";
        $hoseCart[$fromJson[$i + 1]['operationNumber']] = $fromJson[$i + 1]['hoseCart'] ?? "";
        $unitOne[$fromJson[$i + 1]['operationNumber']] = $fromJson[$i + 1]['unitOne'] ?? "";
        $unitTwo[$fromJson[$i + 1]['operationNumber']] = $fromJson[$i + 1]['unitTwo'] ?? "";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Setup</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100 flex items-center justify-center overflow-auto h-[calc(100vh-74px)]">

<div class="w-2/3 bg-white rounded-xl shadow-lg p-6 m-8">

    <h1 class="flex text-3xl font-bold mb-4 justify-center">Setup Einsätze</h1>

    <?php
    if ($numberOfOperations == 0 && empty($_POST)) {
        ?>
        <form action="setup.php" method="get" class="space-y-4">
            <div>
                <label for="numberOfOperations" class="block text-sm font-medium text-gray-700">Einsatzanzahl</label>
                <input type="number" id="numberOfOperations" name="numberOfOperations" class="mt-1 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
            </div>

            <div class="flex justify-center">
                <button type="submit" class="py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                    Weiter
                </button>
            </div>
        </form>
        <?php
    }
    ?>

    <?php
    if (isset($numberOfOperations[1])) {
        echo $numberOfOperations[1];
    }
    ?>

    <?php
    if ($numberOfOperations != 0 && empty($_POST)) {
        ?>
        <form action="setup.php" method="POST" class="space-y-4 divide-y">

            <input name="numberOfOperations" value="<?php echo $numberOfOperations; ?>" hidden>

            <?php
            for ($i = 0; $i < $numberOfOperations; $i++) {
                ?>
                <div class="space-y-4 py-2">
                    <h2 class="text-xl font-bold">Einsatznummer <?php echo $i + 1; ?></h2>

                    <input name="operationNumber<?php echo "-" . ($i + 1); ?>" value="<?php echo $i + 1; ?>" hidden>
                    <div>
                        <label for="operationDescription" class="block text-sm font-medium text-gray-700">Einsatzbeschreibung</label>
                        <input type="text" id="operationDescription" name="operationDescription<?php echo "-" . ($i + 1); ?>"
                               value="<?php echo $operationDescription[$i + 1] ?? ""; ?>" class="mt-1 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                    </div>
                    <div>
                        <label for="address" class="block text-sm font-medium text-gray-700">Adresse</label>
                        <input type="text" id="address" name="address<?php echo "-" . ($i + 1); ?>"
                               value="<?php echo $address[$i + 1] ?? ""; ?>" class="mt-1 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                    </div>
                    <div>
                        <label for="operationDate" class="block text-sm font-medium text-gray-700">Einsatzdatum</label>
                        <input type="date" id="operationDate" name="operationDate<?php echo "-" . ($i + 1); ?>"
                               value="<?php echo $operationDate[$i + 1] ?? ""; ?>" class="mt-1 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                    </div>
                    <div>
                        <label for="operationTime" class="block text-sm font-medium text-gray-700">Einsatzuhrzeit</label>
                        <input type="time" id="operationTime" name="operationTime<?php echo "-" . ($i + 1); ?>"
                               value="<?php echo $operationTime[$i + 1] ?? ""; ?>" class="mt-1 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                    </div>

                    <div class="flex space-x-4 justify-center items-center">
                        <div>
                            <label for="1/19" class="block text-sm font-medium text-gray-700">1/19</label>
                            <input type="checkbox" id="1/19" name="1/19<?php echo "-" . ($i + 1); ?>"
                                <?php if (isset($oneNineteen[$i + 1])) {
                                    if ($oneNineteen[$i + 1] == "on") {
                                        echo "checked";
                                    }
                                } ?> class="mt-1 block h-4 w-4 rounded text-indigo-600 focus:ring-indigo-500 border-gray-300">
                        </div>
                        <div>
                            <label for="1/42" class="block text-sm font-medium text-gray-700">1/42</label>
                            <input type="checkbox" id="1/42" name="1/42<?php echo "-" . ($i + 1); ?>"
                                <?php if (isset($oneFortyTwo[$i + 1])) {
                                    if ($oneFortyTwo[$i + 1] == "on") {
                                        echo "checked";
                                    }
                                } ?> class="mt-1 block h-4 w-4 rounded text-indigo-600 focus:ring-indigo-500 border-gray-300">
                        </div>
                        <div>
                            <label for="2/42" class="block text-sm font-medium text-gray-700">2/42</label>
                            <input type="checkbox" id="2/42" name="2/42<?php echo "-" . ($i + 1); ?>"
                                <?php if (isset($twoFortyTwo[$i + 1])) {
                                    if ($twoFortyTwo[$i + 1] == "on") {
                                        echo "checked";
                                    }
                                } ?> class="mt-1 block h-4 w-4 rounded text-indigo-600 focus:ring-indigo-500 border-gray-300">
                        </div>
                        <div>
                            <label for="3/48" class="block text-sm font-medium text-gray-700">3/48</label>
                            <input type="checkbox" id="3/48" name="3/48<?php echo "-" . ($i + 1); ?>"
                                <?php if (isset($threeFortyEight[$i + 1])) {
                                    if ($threeFortyEight[$i + 1] == "on") {
                                        echo "checked";
                                    }
                                } ?> class="mt-1 block h-4 w-4 rounded text-indigo-600 focus:ring-indigo-500 border-gray-300">
                        </div>
                        <div>
                            <label for="oil" class="block text-sm font-medium text-gray-700">Öl</label>
                            <input type="checkbox" id="oil" name="oil<?php echo "-" . ($i + 1); ?>"
                                <?php if (isset($oil[$i + 1])) {
                                    if ($oil[$i + 1] == "on") {
                                        echo "checked";
                                    }
                                } ?> class="mt-1 block h-4 w-4 rounded text-indigo-600 focus:ring-indigo-500 border-gray-300">
                        </div>
                        <div>
                            <label for="hoseCart" class="block text-sm font-medium text-gray-700">SW</label>
                            <input type="checkbox" id="hoseCart" name="hoseCart<?php echo "-" . ($i + 1); ?>"
                                <?php if (isset($hoseCart[$i + 1])) {
                                    if ($hoseCart[$i + 1] == "on") {
                                        echo "checked";
                                    }
                                } ?> class="mt-1 block h-4 w-4 rounded text-indigo-600 focus:ring-indigo-500 border-gray-300">
                        </div>
                    </div>

                    <div class="flex space-x-4 justify-center items-center">
                        <div>
                            <label for="unitOne" class="block text-sm font-medium text-gray-700">Zug 1</label>
                            <input type="checkbox" id="unitOne" name="unitOne<?php echo "-" . ($i + 1); ?>"
                                <?php if (isset($unitOne[$i + 1])) {
                                    if ($unitOne[$i + 1] == "on") {
                                        echo "checked";
                                    }
                                } ?> class="mt-1 block h-4 w-4 rounded text-indigo-600 focus:ring-indigo-500 border-gray-300">
                        </div>
                        <div>
                            <label for="unitTwo" class="block text-sm font-medium text-gray-700">Zug 2</label>
                            <input type="checkbox" id="unitTwo" name="unitTwo<?php echo "-" . ($i + 1); ?>"
                                <?php if (isset($unitTwo[$i + 1])) {
                                    if ($unitTwo[$i + 1] == "on") {
                                        echo "checked";
                                    }
                                } ?> class="mt-1 block h-4 w-4 rounded text-indigo-600 focus:ring-indigo-500 border-gray-300">
                        </div>
                    </div>

                </div>
                <?php
            }
            ?>

            <button type="submit" class="flex justify-center py-2 px-4 mb-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 mx-auto">
                Speichern
            </button>

        </form>
        <?php
    }
    ?>

<?php
if (!empty($_POST)) {

    $json = "[";

    if (isset($_POST['numberOfOperations']) && $_POST['numberOfOperations'] > 1) {
        $json .= '{"numberOfOperations": "' . $_POST['numberOfOperations'] . '"},';
    }

    for ($i = 0; $i < $_POST['numberOfOperations']; $i++) {
        $postArray = array(
            "operationNumber" => $_POST['operationNumber' . ("-" . ($i + 1))],
            "operationDescription" => $_POST['operationDescription' . ("-" . ($i + 1))],
            "address" => $_POST['address' . ("-" . ($i + 1))],
            "operationDate" => $_POST['operationDate' . ("-" . ($i + 1))],
            "operationTime" => $_POST['operationTime' . ("-" . ($i + 1))],

            "1-19" => $_POST['1/19' . ("-" . ($i + 1))] ?? "off",
            "1-42" => $_POST['1/42' . ("-" . ($i + 1))] ?? "off",
            "2-42" => $_POST['2/42' . ("-" . ($i + 1))] ?? "off",
            "3-48" => $_POST['3/48' . ("-" . ($i + 1))] ?? "off",

            "oil" => $_POST['oil' . ("-" . ($i + 1))] ?? "off",
            "hoseCart" => $_POST['hoseCart' . ("-" . ($i + 1))] ?? "off",
            "unitOne" => $_POST['unitOne' . ("-" . ($i + 1))] ?? "off",
            "unitTwo" => $_POST['unitTwo' . ("-" . ($i + 1))] ?? "off"
        );

        $json .= json_encode($postArray);

        if ($_POST['numberOfOperations'] > $i + 1) {
            $json .= ",";
        }

        if ($_POST['numberOfOperations'] == $i + 1) {
            $json .= "]";
        }

        $file = 'config.json';
    }

    if (isset($file)) {
        file_put_contents($file, $json);
    }
}
?>
<?php
if (!empty($_POST)) {
    ?>
    <h3>Setup erfolgreich abgeschlossen</h3>
    <?php
}
?>
    <a class="flex justify-center text-xs mt-4 text-gray-500" href="third-party-license-notices.html">Third Party License Notice</a>
</body>
</html>
