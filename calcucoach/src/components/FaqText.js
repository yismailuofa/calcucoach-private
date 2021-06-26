export default function FaqText() {
  return (
    <div
      style={{
        fontSize: "3vh",
        width: "80vw",
        maxHeight: "65vh",
        backgroundColor: "#4a86ba",
        padding: "4vh",
        paddingTop: "2vh",
        marginTop: "-6vh",
        borderRadius: "4vh",
        display: "flex",
        flexDirection: "column",
        position: "relative",
        justifyText: "center",
        boxShadow: "0vw 5px 20px black",
        overflow: "auto",
      }}
    >
      Q: What does A x B mean?
      <br />
      <div style={{ fontSize: "2.5vh" }}>
        A: This notation means A sets of B reps. This means you do the exercise
        A times and repeat the motion within the exercise B times.
      </div>
      <br />
      Q: How do I do this exercise?
      <br />
      <div style={{ fontSize: "2.5vh" }}>
        A: All the exercises are designed to be easily found with a Google
        Search. We are working on developing training videos for you to follow
        along with.
      </div>
      <br />
      Q: How long do these workouts take?
      <br />
      <div style={{ fontSize: "2.5vh" }}>
        A: These workouts are designed to take about 1 hour in the gym. This
        depends on things such as experience level and rest time.
      </div>
    </div>
  );
}
