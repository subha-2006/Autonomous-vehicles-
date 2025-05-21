<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Autonomous Vehicle AI Dashboard</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"/>
  <style>
    body {
      background-color: #f8f9fa;
    }
    .login-container {
      max-width: 400px;
      margin: 100px auto;
    }
    .dashboard {
      display: none;
    }
  </style>
</head>
<body>

<!-- Login Form -->
<div class="container login-container" id="loginForm">
  <div class="card shadow">
    <div class="card-body">
      <h4 class="card-title text-center">AI Vehicle Login</h4>
      <div class="mb-3">
        <label for="username" class="form-label">Username</label>
        <input type="text" id="username" class="form-control"/>
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <input type="password" id="password" class="form-control"/>
      </div>
      <button onclick="login()" class="btn btn-primary w-100">Login</button>
      <p class="text-danger mt-2" id="loginError" style="display:none;">Invalid credentials.</p>
    </div>
  </div>
</div>

<!-- Dashboard -->
<div class="container dashboard" id="dashboard">
  <h2 class="my-4">Autonomous Vehicle Dashboard</h2>
  <div class="row mb-4">
    <div class="col-md-4">
      <div class="card border-success shadow">
        <div class="card-body">
          <h5>Status</h5>
          <p>Operational Vehicles: <strong>12</strong></p>
          <p>Offline Vehicles: <strong>2</strong></p>
        </div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card border-warning shadow">
        <div class="card-body">
          <h5>Alerts</h5>
          <p>Low Battery: <strong>3</strong></p>
          <p>Maintenance Required: <strong>1</strong></p>
        </div>
      </div>
    </div>
  </div>

  <h4>Vehicle Details</h4>
  <table class="table table-bordered table-striped">
    <thead>
      <tr>
        <th>ID</th>
        <th>Model</th>
        <th>Status</th>
        <th>Battery (%)</th>
        <th>Last Active</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>AV001</td>
        <td>Model X</td>
        <td>Online</td>
        <td>87</td>
        <td>10 mins asgo</td>
      </tr>
      <tr>
        <td>AV002</td>
        <td>Model Z</td>
        <td>Online</td>
        <td>75</td>
        <td>5 mins ago</td>
      </tr>
      <tr>
        <td>AV003</td>
        <td>Model S</td>
        <td>Offline</td>
        <td>--</td>
        <td>1 hour ago</td>
      </tr>
    </tbody>
  </table>

  <button class="btn btn-secondary mt-3" onclick="logout()">Logout</button>
</div>

<script>
  function login() {
    const user = document.getElementById("username").value;
    const pass = document.getElementById("password").value;
    const error = document.getElementById("loginError");

    if (user === "admin" && pass === "admin123") {
      document.getElementById("loginForm").style.display = "none";
      document.getElementById("dashboard").style.display = "block";
      error.style.display = "none";
    } else {
      error.style.display = "block";
    }
  }

  function logout() {
    document.getElementById("dashboard").style.display = "none";
    document.getElementById("loginForm").style.display = "block";
  }
</script>

</body>
</html>