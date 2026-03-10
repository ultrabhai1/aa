<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notica · Stress Test UI</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Roboto, system-ui, sans-serif;
        }

        body {
            background: #0b0f17;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }

        .card {
            max-width: 900px;
            width: 100%;
            background: #131a2c;
            border-radius: 28px;
            padding: 30px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6), 0 0 0 1px #2a3a55 inset;
            color: #e0e5f0;
        }

        /* Top warning message */
        .warning {
            background: #1e2a3a;
            border-left: 6px solid #f0b400;
            border-radius: 18px;
            padding: 16px 22px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 30px;
            box-shadow: 0 6px 14px rgba(0,0,0,0.4);
        }
        .warning p {
            font-size: 1.1rem;
            font-weight: 500;
            color: #ffd966;
        }
        .ok-btn {
            background: #2d405b;
            border: none;
            color: white;
            font-weight: 600;
            font-size: 1rem;
            padding: 8px 28px;
            border-radius: 40px;
            cursor: pointer;
            transition: 0.2s;
            box-shadow: 0 2px 6px rgba(0,0,0,0.3);
            letter-spacing: 0.5px;
        }
        .ok-btn:hover {
            background: #3e5577;
            transform: scale(1.02);
        }

        /* Concurrents + Send Attack row */
        .concurrent-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: #101826;
            border-radius: 60px;
            padding: 12px 25px 12px 30px;
            margin-bottom: 35px;
            border: 1px solid #2b3f5c;
        }
        .concurrent-label {
            font-size: 1.4rem;
            font-weight: 600;
            color: #b7c9e2;
            letter-spacing: 1px;
        }
        .concurrent-number {
            font-size: 2rem;
            font-weight: 800;
            background: linear-gradient(145deg, #a3c6ff, #5b8cff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-left: 12px;
        }
        .send-btn {
            background: linear-gradient(145deg, #2658b8, #103780);
            border: none;
            color: white;
            font-size: 1.5rem;
            font-weight: 700;
            padding: 14px 48px;
            border-radius: 60px;
            cursor: pointer;
            box-shadow: 0 10px 18px rgba(0, 30, 100, 0.6);
            transition: 0.15s;
            letter-spacing: 1.5px;
            border: 1px solid #3f7eff;
        }
        .send-btn:hover {
            background: linear-gradient(145deg, #2f6be0, #154ab0);
            transform: scale(1.02);
            box-shadow: 0 12px 22px #00227766;
        }

        /* History table */
        .history-title {
            font-size: 1.8rem;
            font-weight: 600;
            margin-bottom: 18px;
            color: #d0ddff;
            border-bottom: 2px solid #253449;
            padding-bottom: 8px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            background: #0f172b;
            border-radius: 24px;
            overflow: hidden;
            box-shadow: 0 8px 20px #00000040;
            margin-bottom: 35px;
            border: 1px solid #2a3850;
        }
        th {
            text-align: left;
            padding: 16px 18px;
            background: #1d2a41;
            color: #a5c1ff;
            font-weight: 600;
            font-size: 1.1rem;
            letter-spacing: 0.3px;
        }
        td {
            padding: 16px 18px;
            border-top: 1px solid #25344a;
            color: #cdddfa;
            font-weight: 400;
        }
        .status-active {
            background: #1e3b2e;
            color: #7cf9b0;
            font-weight: 600;
            padding: 6px 14px;
            border-radius: 40px;
            display: inline-block;
            font-size: 0.9rem;
        }

        /* Upgrade section */
        .upgrade-box {
            background: linear-gradient(145deg, #1e2640, #131b30);
            border-radius: 30px;
            padding: 24px 30px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 30px;
            border: 1px solid #4a6085;
            box-shadow: 0 6px 0 #0b101c;
        }
        .upgrade-text {
            font-size: 1.6rem;
            font-weight: 700;
            background: linear-gradient(145deg, #ffe791, #ccb055);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .upgrade-btn {
            background: #fedb5f;
            border: none;
            color: #0b0f17;
            font-weight: 800;
            font-size: 1.3rem;
            padding: 16px 40px;
            border-radius: 60px;
            cursor: pointer;
            box-shadow: 0 8px 0 #9e7e30, 0 10px 20px black;
            transition: 0.07s linear;
            border: 1px solid #ffed9e;
        }
        .upgrade-btn:active {
            transform: translateY(6px);
            box-shadow: 0 2px 0 #9e7e30, 0 10px 20px black;
        }

        /* Network slots */
        .slots-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #0e1629;
            border-radius: 80px;
            padding: 20px 30px;
            border: 1px solid #364b6e;
        }
        .slots-label {
            font-size: 1.4rem;
            font-weight: 600;
            color: #a3bbdc;
        }
        .slots-numbers {
            font-size: 2rem;
            font-weight: 700;
            background: linear-gradient(145deg, #bbd4ff, #7faaef);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .in-use {
            background: #1f334e;
            padding: 12px 30px;
            border-radius: 60px;
            font-size: 1.3rem;
            color: #b5d0ff;
            font-weight: 500;
            border: 1px solid #4f71a5;
        }

        /* Dismiss alert functionality */
        .hidden {
            display: none !important;
        }
    </style>
</head>
<body>
    <div class="card">
        <!-- Warning message (like in image) -->
        <div class="warning" id="warningBanner">
            <p>⚠️ Match server response timed out. Please check your network.</p>
            <button class="ok-btn" id="dismissWarning">OK</button>
        </div>

        <!-- Concurrents + Send Attack row -->
        <div class="concurrent-row">
            <div style="display: flex; align-items: center;">
                <span class="concurrent-label">Concurrents</span>
                <span class="concurrent-number">1</span>
            </div>
            <button class="send-btn" id="sendAttackBtn">SEND ATTACK</button>
        </div>

        <!-- History table -->
        <div class="history-title">⚡ History</div>
        <table>
            <thead>
                <tr>
                    <th>Target</th>
                    <th>Method</th>
                    <th>Time</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>20.198.82.124:26635</td>
                    <td>UDP-FREE</td>
                    <td>120s</td>
                    <td><span class="status-active">1:49</span></td>
                </tr>
                <!-- Extra row to show style, you can remove if only one needed -->
                <tr style="opacity:0.7;">
                    <td>192.168.1.45:8080</td>
                    <td>TCP-MIX</td>
                    <td>60s</td>
                    <td><span style="background:#3a2f4a; color:#cfaaff; padding:6px 14px; border-radius:40px;">completed</span></td>
                </tr>
            </tbody>
        </table>

        <!-- Upgrade for 10x Power -->
        <div class="upgrade-box">
            <span class="upgrade-text">🚀 Upgrade for 10x Power</span>
            <button class="upgrade-btn" id="upgradeBtn">UPGRADE NOW</button>
        </div>

        <!-- Network Slots -->
        <div class="slots-container">
            <span class="slots-label">Free Network</span>
            <span class="slots-numbers">9 / 10</span>
            <span class="in-use">1 in use</span>
        </div>
    </div>

    <script>
        // Dismiss the warning banner
        document.getElementById('dismissWarning').addEventListener('click', function() {
            document.getElementById('warningBanner').classList.add('hidden');
        });

        // Send Attack button – just a demo simulation
        document.getElementById('sendAttackBtn').addEventListener('click', function() {
            alert('🚀 Attack simulation started (localhost test only).\nCheck your network tool for real traffic.');
            // Optionally you could add a dummy history row, but keeping simple.
        });

        // Upgrade button – demo
        document.getElementById('upgradeBtn').addEventListener('click', function() {
            alert('✨ Upgrade feature – this is a demo UI. No actual upgrade.');
        });

        // Optional: simulate that the warning can be shown again? Not needed.
    </script>
</body>
</html>
