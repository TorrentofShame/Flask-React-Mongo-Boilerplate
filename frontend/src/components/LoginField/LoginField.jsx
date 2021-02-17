import React from "react";

import { Login } from "_api/auth";

class LoginField extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      username: "",
      password: ""
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({
      [event.target.name]: event.target.value
    });
  }

  handleSubmit(event) {
    event.preventDefault();

    let userCreds = {
      this.state.username,
      this.state.password
    };
    Login(userCreds);
    // TODO: Set session storage data to store the jwt token that we get.
  }

  render() {
    <section
      style={{
        display: "flex",
        alignItems: "center",
        justifyContent: "center"
      }}
    >
      <div>
        <h1>Login Form</h1>
        <form onSubmit={this.handleSubmit}>
          <label>Username:
            <input
              type="text"
              value={this.state.username}
              onChange={this.handleChange}
            />
          </label>
          <label>
            Password:
            <input
              type="password"
              value={this.state.password}
              onChange={this.handleChange}
            />
          </label>
          <input type="submit" value="Login" />
        </form>
      </div>
    </section>
  }
}

export default LoginField;
