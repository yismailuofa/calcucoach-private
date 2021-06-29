import { useRef, useState } from "react";
import { CSSTransition } from "react-transition-group";
import BackButton from "./BackButton";
import programs from "../programs.json";
import "./styles/slideX.css";

export default function WorkoutStyles({
  nextStep,
  prevStep,
  setStyle,
  step,
  isFaq,
}) {
  const [animationDirection, setanimationDirection] = useState("slideXmiddle");
  const nodeRef = useRef(null);

  const handleBack = () => {
    setanimationDirection("slideXfront");
    prevStep();
  };

  return (
    <CSSTransition
      in={step === 2 && !isFaq}
      timeout={900}
      classNames={animationDirection}
      unmountOnExit={true}
      nodeRef={nodeRef}
      onExited={() =>
        animationDirection === "slideXmiddle" &&
        setanimationDirection("slideXbehind")
      }
      onEntered={() => setanimationDirection("slideXmiddle")}
    >
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          position: "absolute",
        }}
        ref={nodeRef}
      >
        <div
          style={{
            fontSize: "3.5vh",
            background:
              "linear-gradient(180deg, rgba(74,134,186,1) 50%, rgba(51,96,136,1) 100%)",
            paddingTop: "4vh",
            paddingBottom: "4vh",
            paddingRight: "1vh",
            paddingLeft: "1vh",
            marginTop: "1vh",
            marginLeft: "3vh",
            marginRight: "3vh",
            borderRadius: "4vh",
            display: "flex",
            flexDirection: "column",
            textAlign: "center",
            boxShadow: "0vw 5px 20px black",
          }}
        >
          What is your workout style?
        </div>
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(3,auto)",
            justifyContent: "center",
            justifyText: "center",
          }}
        >
          {Object.keys(programs.maleProgramsList).map((key) => (
            <div
              key={key}
              style={{
                background:
                  "linear-gradient(180deg, rgba(74,134,186,1) 50%, rgba(51,96,136,1) 100%)",
                margin: "1vh",
                padding: "1vh",
                borderRadius: "10px",
                display: "flex",
                flexDirection: "column",
                justifyContent: "center",
                alignItems: "center",
                fontSize: "1vh",
              }}
            >
              <img
                src="https://cdn.iconscout.com/icon/free/png-256/barbell-dumbbell-dumbell-fitness-gym-weight-weightlifting-6-17867.png"
                alt="test"
                height="64px"
                width="64px"
              ></img>
              {programs.maleProgramsList[key]}
            </div>
          ))}
        </div>
        <BackButton onClick={handleBack} />
      </div>
    </CSSTransition>
  );
}
