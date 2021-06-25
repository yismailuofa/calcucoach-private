import Header from "./Header";
import Jumbotron from "./Jumbotron";
import { Component } from "react";

export default class App extends Component {
  constructor(props) {
    super(props)

    this.state = {
      step: 0,
    }
  }

  prevStep = (e) => {
    e.preventDefault()
    e.stopPropagation()
    this.setState({
      step: this.state.step - 1
    })
  }

  render() {
    return (
      <div
        style={{
          display: "flex",
          height: "100vh",
          flexDirection: "column",
          alignItems: "center",
          color: "white",
          letterSpacing: "-0.06em",
        }}
      >
        <Header />
        <Jumbotron />
      </div>
    );
  }
}
