import { Component } from "react";
import Header from "./Header";
import Jumbotron from "./Jumbotron";

export default class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      step: 0,
      isFaq: false,
    };
  }

  faqShow = (e) => {
    this.setState({
      isFaq: true,
    });
  };

  faqHide = (e) => {
    this.setState({
      isFaq: false,
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
        <Header faqShow={this.faqShow} />
        <Jumbotron
          step={this.state.step}
          isFaq={this.state.isFaq}
          prevStep={this.prevStep}
          nextStep={this.nextStep}
          faqHide={this.faqHide}
        />
      </div>
    );
  }
}
