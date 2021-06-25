import { Component } from "react";
import banner from "../assets/banner.jpg";
import bannerBlurred from "../assets/bannerBlurred.jpg";
import IntroText from "./IntroText";

export default class Jumbotron extends Component {
  constructor(props) {
    super(props);

    this.state = {
      step: 0,
    };
  }

  prevStep = () => {
    console.log("joon")
    this.setState({
      step: this.state.step - 1,
    });
  };

  render() {
    const isBlur = this.state.step !== 0
    const bannerImg = isBlur ? bannerBlurred : banner
    return (
      <div
        style={{
          backgroundImage: `url(${bannerImg})`,
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
        <IntroText prevStep={this.prevStep}/>
      </div>
    );
  }
}
