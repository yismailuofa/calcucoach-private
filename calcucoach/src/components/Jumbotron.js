import banner from "../assets/banner.jpg";
import bannerBlurred from "../assets/bannerBlurred.jpg";
import IntroText from "./IntroText";
import FaqText from "./FaqText";
import FaqBack from "./FaqBack";

export default function Jumbotron(props) {
  const isBlur = props.step < 0;
  const bannerImg = isBlur ? bannerBlurred : banner;
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
        transition: "background-image .7s linear",
      }}
    >
      {props.step === -1 && (
        <>
          <FaqText /> <FaqBack nextStep={props.nextStep}/>
        </>
      )}
      {props.step === 0 && <IntroText />}
    </div>
  );
}
