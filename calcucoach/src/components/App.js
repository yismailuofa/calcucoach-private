import { Component } from "react";
import Header from "./Header";
import Jumbotron from "./Jumbotron";

export default class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      step: 0,
    };
  }

  faqStep = (e) => {
    this.setState({
      step: -1,
    });
  };
  prevStep = (e) => {
    this.setState({
      step: this.state.step - 1,
    });
  };

  nextStep = (e) => {
    this.setState({
      step: this.state.step + 1,
    });
  };

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
        <Header faqStep={this.faqStep}/>
        <Jumbotron step={this.state.step} prevStep={this.prevStep} nextStep={this.nextStep}/>
      </div>
    );
  }
}
