import banner from "../assets/banner.jpg";
import StartText from "./StartText";
import FaqScreen from "./FaqScreen";
import { Component } from "react";

export default class Jumbotron extends Component {
  constructor(props) {
    super(props);
    this.state = {
      step: 0,
      gender: "male",
      workoutStyle: 0,
      workoutDays: 3,
    };
  }

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
          backgroundImage: `url(${banner})`,
          width: "100vw",
          height: "100vh",
          backgroundSize: "cover",
          backgroundPosition: "45% 55%",
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",          
        }}
      >
        <FaqScreen faqHide={this.props.faqHide} isFaq={this.props.isFaq}/>
        <StartText
          nextStep={this.nextStep}
          step={this.state.step}
          isFaq={this.props.isFaq}
        />
      </div>
    );
  }
}
