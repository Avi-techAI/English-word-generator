from __future__ import annotations

import argparse
import json
import random
import sys
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA_PATH = PROJECT_ROOT / "data" / "words.json"
DEFAULT_README_PATH = PROJECT_ROOT / "README.md"
DEFAULT_TIMEZONE = "Europe/London"

README_STATS_START = "<!-- WORD_STATS_START -->"
README_STATS_END = "<!-- WORD_STATS_END -->"

RAW_WORD_BANK = """
abundant|adjective|beginner|more than enough in amount|The town has abundant green space.
adapt|verb|beginner|to change so something works in a new situation|Good learners adapt when plans change.
admire|verb|beginner|to respect or like someone or something|I admire her calm way of speaking.
agile|adjective|intermediate|able to move or think quickly|The team stayed agile during the launch.
analyze|verb|intermediate|to study something carefully to understand it|We analyze the results every Friday.
ancient|adjective|beginner|very old or from a long time ago|The museum displayed ancient coins.
anxious|adjective|beginner|worried or nervous about something|He felt anxious before the interview.
apparent|adjective|intermediate|easy to see or understand|The reason for the delay soon became apparent.
aspire|verb|intermediate|to strongly want to achieve something|Many students aspire to study abroad.
balance|noun|beginner|a steady state where different parts are equal or controlled|A healthy life needs balance.
barrier|noun|beginner|something that blocks movement or progress|Language can be a barrier at first.
benefit|noun|beginner|a helpful or useful result|Daily practice has a clear benefit.
bold|adjective|beginner|confident and willing to take risks|She made a bold decision.
brief|adjective|beginner|short in time or length|We had a brief meeting after lunch.
capable|adjective|beginner|having the skill or ability to do something|You are capable of learning quickly.
capture|verb|intermediate|to catch, record, or describe something well|The photo captures the mood of the city.
cautious|adjective|intermediate|careful to avoid danger or mistakes|Be cautious when sharing personal data.
cherish|verb|intermediate|to value and care about something deeply|They cherish their family traditions.
clarify|verb|intermediate|to make something easier to understand|Please clarify the final deadline.
coherent|adjective|advanced|clear, logical, and easy to follow|Her report was coherent and persuasive.
collaborate|verb|intermediate|to work with others toward a shared goal|Designers and engineers collaborate every day.
comfort|noun|beginner|a feeling of ease, safety, or relief|Music gave him comfort after a long day.
concise|adjective|intermediate|using few words while staying clear|A concise answer is often stronger.
confident|adjective|beginner|sure about your ability or decision|She sounded confident during the call.
curious|adjective|beginner|wanting to learn or know more|Curious people ask better questions.
debate|noun|intermediate|a serious discussion with different opinions|The class held a debate about technology.
declare|verb|intermediate|to say something clearly or officially|The judge will declare the winner.
delicate|adjective|intermediate|easily damaged or needing careful handling|The vase is delicate.
deliberate|adjective|advanced|done carefully and intentionally|The change was deliberate, not accidental.
dependable|adjective|intermediate|able to be trusted to do what is needed|A dependable friend arrives on time.
diverse|adjective|intermediate|including many different kinds of people or things|The city has a diverse food scene.
eager|adjective|beginner|very interested and excited to do something|The children were eager to begin.
efficient|adjective|intermediate|working well without wasting time or energy|The new process is more efficient.
elaborate|verb|advanced|to add more detail or explanation|Could you elaborate on your idea?
emerge|verb|intermediate|to appear or become known|A new pattern began to emerge.
empathy|noun|intermediate|the ability to understand another person's feelings|Empathy helps teams work better.
endure|verb|intermediate|to continue through something difficult|The old bridge endured many storms.
enhance|verb|intermediate|to improve the quality or value of something|Practice can enhance your writing.
essential|adjective|beginner|absolutely necessary or very important|Water is essential for life.
evaluate|verb|intermediate|to judge the value or quality of something|We evaluate each option carefully.
evident|adjective|intermediate|clear and easy to notice|Her progress was evident to everyone.
expand|verb|beginner|to become larger or make something larger|The company plans to expand next year.
explore|verb|beginner|to look around or study something new|They explore a new topic each week.
faithful|adjective|intermediate|loyal and reliable|The dog was a faithful companion.
flexible|adjective|beginner|able to change or bend easily|A flexible schedule reduces stress.
flourish|verb|advanced|to grow or succeed strongly|Small businesses can flourish online.
focus|verb|beginner|to give attention to one thing|Focus on one task at a time.
forecast|noun|intermediate|a prediction about what may happen|The weather forecast predicts rain.
frequent|adjective|beginner|happening often|Frequent breaks can improve focus.
generous|adjective|beginner|willing to give more than expected|He made a generous donation.
genuine|adjective|intermediate|real, honest, and sincere|Her smile seemed genuine.
gradual|adjective|intermediate|happening slowly over time|The improvement was gradual.
grateful|adjective|beginner|feeling thankful|I am grateful for your help.
harmony|noun|intermediate|a peaceful or pleasing agreement|The colors worked in harmony.
hesitate|verb|intermediate|to pause before doing or saying something|Do not hesitate to ask questions.
humble|adjective|intermediate|not acting more important than others|The champion remained humble.
ideal|adjective|beginner|perfect or most suitable|This room is ideal for studying.
illustrate|verb|intermediate|to explain or show something with examples|The chart illustrates the trend.
impact|noun|beginner|a strong effect or influence|The teacher had a lasting impact.
improve|verb|beginner|to become better or make something better|Daily reading can improve vocabulary.
insight|noun|intermediate|a clear understanding of something|The interview gave us useful insight.
inspire|verb|beginner|to make someone feel ready to do something good|Her story can inspire many people.
integrity|noun|advanced|honesty and strong moral principles|Integrity matters in leadership.
invent|verb|beginner|to create something new|They hope to invent a better tool.
journey|noun|beginner|a trip or long process of change|Learning is a journey.
joyful|adjective|beginner|very happy|The room felt joyful after the news.
justice|noun|intermediate|fair treatment under rules or law|The group worked for justice.
keen|adjective|intermediate|very interested or eager|She is keen to learn Python.
knowledge|noun|beginner|information and understanding gained by learning|Books help build knowledge.
labor|noun|intermediate|hard physical or mental work|The project required months of labor.
lasting|adjective|beginner|continuing for a long time|Kind words can have a lasting effect.
logical|adjective|intermediate|reasonable and based on clear thinking|The plan followed a logical order.
maintain|verb|intermediate|to keep something in good condition or continue it|Regular updates maintain the app.
mature|adjective|intermediate|fully developed or sensible|Her mature response impressed them.
method|noun|beginner|a planned way of doing something|This method saves time.
mindful|adjective|intermediate|aware and careful about something|Be mindful of your tone.
modest|adjective|intermediate|not too large, proud, or showy|They started with a modest budget.
motive|noun|intermediate|a reason for doing something|The detective searched for a motive.
natural|adjective|beginner|existing in nature or happening easily|The speech sounded natural.
navigate|verb|intermediate|to find a way through or deal with something|Students navigate many choices.
notable|adjective|intermediate|important or worth noticing|The app had notable improvements.
observe|verb|beginner|to watch or notice carefully|Observe how people use the feature.
obtain|verb|intermediate|to get something|You must obtain permission first.
patient|adjective|beginner|able to wait calmly|A patient teacher helps beginners.
pattern|noun|beginner|a repeated form, design, or behavior|We noticed a pattern in the data.
peaceful|adjective|beginner|calm and free from trouble|The park was peaceful in the morning.
persist|verb|intermediate|to continue despite difficulty|If you persist, your skill will grow.
precise|adjective|intermediate|exact and accurate|Use precise words in instructions.
predict|verb|beginner|to say what may happen in the future|Can you predict the next result?
prepare|verb|beginner|to get ready|Prepare your notes before the meeting.
priority|noun|intermediate|something more important than other things|Health should be a priority.
progress|noun|beginner|movement toward improvement or a goal|Small progress still counts.
protect|verb|beginner|to keep someone or something safe|Strong passwords protect accounts.
purpose|noun|beginner|the reason something exists or is done|The purpose of the app is learning.
quality|noun|beginner|how good or useful something is|Quality matters more than speed.
radiant|adjective|advanced|bright, warm, or full of happiness|She had a radiant smile.
rare|adjective|beginner|not happening or found often|It was a rare opportunity.
reflect|verb|intermediate|to think carefully or show an image|Reflect on what you learned today.
reliable|adjective|beginner|able to be trusted|The script gives reliable results.
resilient|adjective|advanced|able to recover after difficulty|Resilient people keep going.
resource|noun|intermediate|something useful that helps you do work|The guide became a helpful resource.
restore|verb|intermediate|to bring something back to a good state|Sleep can restore your energy.
reveal|verb|beginner|to show something that was hidden|The test will reveal the issue.
rhythm|noun|intermediate|a regular pattern of sound or movement|The poem has a gentle rhythm.
secure|adjective|beginner|safe and protected|Keep your account secure.
sincere|adjective|intermediate|honest and truly meant|He gave a sincere apology.
skillful|adjective|intermediate|showing ability and practice|The chef made a skillful cut.
solution|noun|beginner|an answer to a problem|We found a simple solution.
steady|adjective|beginner|controlled, regular, and not shaking|Steady practice builds confidence.
strategy|noun|intermediate|a plan for reaching a goal|Their strategy was simple and clear.
subtle|adjective|advanced|not obvious but still important|The design used subtle colors.
thrive|verb|advanced|to grow, succeed, or do very well|Plants thrive with enough light.
tolerant|adjective|intermediate|willing to accept differences|A tolerant community welcomes debate.
transform|verb|intermediate|to change completely|The course can transform your habits.
unique|adjective|beginner|being the only one of its kind|Every learner has a unique path.
urgent|adjective|beginner|needing quick action|The message sounded urgent.
valuable|adjective|beginner|useful or worth a lot|Feedback is valuable for improvement.
verify|verb|intermediate|to check that something is true or correct|Always verify important information.
vivid|adjective|intermediate|clear, bright, and detailed|She wrote a vivid description.
wander|verb|beginner|to walk without a fixed plan|They wander through the market.
wisdom|noun|intermediate|good judgment gained from experience|Wisdom often comes with patience.
worthy|adjective|intermediate|deserving respect, effort, or attention|It is a worthy goal.
ambiguous|adjective|advanced|having more than one possible meaning|The instruction was ambiguous.
articulate|verb|advanced|to express an idea clearly|She can articulate complex ideas.
audacious|adjective|advanced|brave, surprising, and willing to take risks|The startup made an audacious promise.
catalyst|noun|advanced|something that causes change or action|The failure became a catalyst for growth.
compelling|adjective|advanced|very interesting or persuasive|The speaker made a compelling argument.
comprehend|verb|intermediate|to understand something fully|It took time to comprehend the rule.
cultivate|verb|advanced|to develop a skill, habit, or relationship|Writers cultivate curiosity.
diligent|adjective|advanced|careful and hardworking|A diligent student reviews mistakes.
dynamic|adjective|intermediate|active, changing, or full of energy|The city has a dynamic culture.
eloquent|adjective|advanced|clear, powerful, and graceful in speech or writing|Her eloquent speech moved the audience.
feasible|adjective|advanced|possible and practical to do|The plan is feasible with a small team.
friction|noun|advanced|difficulty or resistance between things|Good design reduces friction.
hypothesis|noun|advanced|an idea tested through study or experiment|The scientist formed a hypothesis.
immerse|verb|advanced|to involve yourself deeply in something|Immerse yourself in English media.
implication|noun|advanced|a possible result or meaning of something|The change has a serious implication.
innovate|verb|advanced|to create or improve with new ideas|Small teams can innovate quickly.
meticulous|adjective|advanced|very careful about small details|The editor was meticulous.
momentum|noun|advanced|the force that keeps progress moving|The project gained momentum.
nuance|noun|advanced|a small but important difference in meaning|Tone adds nuance to a sentence.
optimize|verb|advanced|to make something work as well as possible|We optimize the script for clarity.
perspective|noun|intermediate|a way of seeing or thinking about something|Travel changed his perspective.
pragmatic|adjective|advanced|focused on practical results|A pragmatic plan is easier to follow.
profound|adjective|advanced|deep, strong, or very meaningful|The book had a profound effect.
rationale|noun|advanced|the reason behind a decision or belief|Explain the rationale for the change.
refine|verb|advanced|to improve by making small changes|We refine the quiz after feedback.
reinforce|verb|advanced|to strengthen or support something|Examples reinforce learning.
skeptical|adjective|advanced|not easily convinced|She remained skeptical of the claim.
sustainable|adjective|advanced|able to continue without causing harm or running out|The team chose a sustainable pace.
transparent|adjective|advanced|open, clear, and easy to understand|Transparent rules build trust.
versatile|adjective|advanced|able to be used in many different ways|Python is a versatile language.
benevolent|adjective|advanced|kind and wanting to help others|The charity had a benevolent mission.
candid|adjective|advanced|honest and direct|She gave candid feedback.
austere|adjective|advanced|plain, strict, or without decoration|The room had an austere style.
vibrant|adjective|intermediate|full of life, color, or energy|The market was vibrant at night.
solace|noun|advanced|comfort during sadness or difficulty|Reading gave him solace.
scarcity|noun|advanced|a lack of enough of something|Scarcity can increase demand.
remedy|noun|intermediate|a solution or treatment for a problem|Rest is a simple remedy for tiredness.
assert|verb|advanced|to state something confidently|The author asserts a clear opinion.
fluent|adjective|intermediate|able to speak or write smoothly|She became fluent through practice.
tranquil|adjective|advanced|quiet and peaceful|The lake was tranquil at sunrise.
glimpse|noun|intermediate|a quick look|We caught a glimpse of the sea.
lavish|adjective|advanced|very rich, large, or generous|The hotel served a lavish breakfast.
fragile|adjective|intermediate|easy to break or damage|Trust can be fragile.
linger|verb|advanced|to stay longer than expected|The smell of coffee lingered.
nurture|verb|advanced|to care for and help something grow|Teachers nurture confidence.
quest|noun|intermediate|a long search for something important|The hero began a quest.
routine|noun|beginner|a regular way of doing things|A morning routine helps focus.
summon|verb|advanced|to call or gather someone or something|She tried to summon her courage.
terrain|noun|intermediate|an area of land and its physical features|The hikers crossed rocky terrain.
unify|verb|advanced|to bring parts together into one|A shared goal can unify a team.
venture|noun|advanced|a risky or exciting new activity|The app became their first venture.
weave|verb|intermediate|to form something by crossing parts together|The story weaves humor with history.
yield|verb|advanced|to produce or give way|Careful study can yield strong results.
zeal|noun|advanced|great energy and enthusiasm|She worked with zeal.
alliance|noun|advanced|a group or partnership formed for a shared purpose|The companies formed an alliance.
brisk|adjective|intermediate|quick, active, or cool|They took a brisk walk.
credible|adjective|advanced|believable and trustworthy|Use credible sources.
discern|verb|advanced|to notice or understand something with care|It is hard to discern the difference.
empower|verb|intermediate|to give someone confidence, authority, or ability|Good tools empower users.
foster|verb|advanced|to encourage growth or development|The club fosters creativity.
graceful|adjective|intermediate|smooth, attractive, or polite|She gave a graceful answer.
hinder|verb|advanced|to slow down or make progress difficult|Poor planning can hinder progress.
inquire|verb|intermediate|to ask for information|You can inquire at the front desk.
legacy|noun|intermediate|something left behind from the past|Her legacy inspired others.
mentor|noun|intermediate|an experienced person who guides someone|A mentor can speed up learning.
orient|verb|advanced|to help someone understand their position or situation|The map helps visitors orient themselves.
pledge|verb|advanced|to promise seriously|They pledge to protect the forest.
robust|adjective|advanced|strong and able to handle problems|The test suite makes the app robust.
shortage|noun|intermediate|a lack of something needed|The area faced a water shortage.
tribute|noun|advanced|something said or done to show respect|The song was a tribute to her teacher.
uphold|verb|advanced|to support or defend a rule or value|Judges uphold the law.
virtue|noun|advanced|a good moral quality|Patience is a virtue.
wary|adjective|advanced|careful because something may be risky|Be wary of unknown links.
"""


def parse_word_bank() -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    seen: set[str] = set()

    for line in RAW_WORD_BANK.strip().splitlines():
        word, part_of_speech, difficulty, definition, example = line.split("|", 4)
        key = word.lower()
        if key in seen:
            raise ValueError(f"Duplicate word in word bank: {word}")
        seen.add(key)
        entries.append(
            {
                "word": word,
                "part_of_speech": part_of_speech,
                "difficulty": difficulty,
                "definition": definition,
                "example": example,
            }
        )

    return entries


WORD_BANK = parse_word_bank()


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def new_data_file() -> dict:
    return {
        "project": "Daily English Word Generator",
        "created_at": utc_timestamp(),
        "updated_at": utc_timestamp(),
        "words": [],
    }


def load_data(path: Path = DEFAULT_DATA_PATH) -> dict:
    if not path.exists():
        return new_data_file()

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    data.setdefault("project", "Daily English Word Generator")
    data.setdefault("created_at", utc_timestamp())
    data.setdefault("updated_at", utc_timestamp())
    data.setdefault("words", [])
    return data


def save_data(data: dict, path: Path = DEFAULT_DATA_PATH) -> None:
    data["updated_at"] = utc_timestamp()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        file.write("\n")


def choose_entries(count: int, seed: str | None = None) -> list[dict[str, str]]:
    if count > len(WORD_BANK):
        raise ValueError(f"Requested {count} words, but the bank only has {len(WORD_BANK)}.")

    entries = [entry.copy() for entry in WORD_BANK]
    rng = random.Random(seed) if seed is not None else random.SystemRandom()
    rng.shuffle(entries)
    return entries[:count]


def with_metadata(entry: dict[str, str], date_added: str, source: str) -> dict[str, str]:
    result = entry.copy()
    result["date_added"] = date_added
    result["source"] = source
    return result


def initialize_words(
    count: int = 100,
    path: Path = DEFAULT_DATA_PATH,
    seed: str | None = None,
    overwrite: bool = False,
    date_added: str | None = None,
) -> dict:
    if path.exists() and not overwrite:
        raise FileExistsError(f"{path} already exists. Use --overwrite to replace it.")

    today = date_added or datetime.now(ZoneInfo(DEFAULT_TIMEZONE)).date().isoformat()
    data = new_data_file()
    data["words"] = [with_metadata(entry, today, "initial") for entry in choose_entries(count, seed)]
    save_data(data, path)
    return data


def available_entries(data: dict) -> list[dict[str, str]]:
    used_words = {item["word"].lower() for item in data.get("words", [])}
    return [entry.copy() for entry in WORD_BANK if entry["word"].lower() not in used_words]


def add_daily_word(
    path: Path = DEFAULT_DATA_PATH,
    timezone_name: str = DEFAULT_TIMEZONE,
    require_local_hour: int | None = None,
    now: datetime | None = None,
    seed: str | None = None,
) -> tuple[bool, str, dict]:
    current_time = now or datetime.now(ZoneInfo(timezone_name))
    if current_time.tzinfo is None:
        current_time = current_time.replace(tzinfo=ZoneInfo(timezone_name))

    local_time = current_time.astimezone(ZoneInfo(timezone_name))
    if require_local_hour is not None and local_time.hour != require_local_hour:
        return (
            False,
            f"Skipped: local time in {timezone_name} is {local_time:%H:%M}, not {require_local_hour:02d}:00.",
            load_data(path),
        )

    target_date = local_time.date().isoformat()
    data = load_data(path)

    if any(
        item.get("date_added") == target_date and item.get("source") == "daily"
        for item in data.get("words", [])
    ):
        return False, f"Skipped: a daily word already exists for {target_date}.", data

    candidates = available_entries(data)
    if not candidates:
        raise RuntimeError("No unused words remain. Add more entries to RAW_WORD_BANK.")

    rng = random.Random(seed) if seed is not None else random.SystemRandom()
    entry = with_metadata(rng.choice(candidates), target_date, "daily")
    data["words"].append(entry)
    save_data(data, path)
    return True, f"Added daily word: {entry['word']} ({entry['part_of_speech']}).", data


def latest_word(data: dict) -> dict | None:
    words = data.get("words", [])
    return words[-1] if words else None


def readme_stats_block(data: dict) -> str:
    latest = latest_word(data)
    if latest is None:
        body = "No words have been added yet."
    else:
        body = "\n".join(
            [
                f"- Total words: **{len(data.get('words', []))}**",
                f"- Latest word: **{latest['word']}** ({latest['part_of_speech']}, {latest['difficulty']})",
                f"- Meaning: {latest['definition']}",
                f"- Example: {latest['example']}",
                f"- Last added: {latest['date_added']}",
            ]
        )

    return f"{README_STATS_START}\n{body}\n{README_STATS_END}"


def update_readme(data: dict, readme_path: Path = DEFAULT_README_PATH) -> None:
    block = readme_stats_block(data)
    if readme_path.exists():
        content = readme_path.read_text(encoding="utf-8")
    else:
        content = "# Daily English Word Generator\n\n"

    if README_STATS_START in content and README_STATS_END in content:
        before = content.split(README_STATS_START, 1)[0].rstrip()
        after = content.split(README_STATS_END, 1)[1].lstrip()
        content = f"{before}\n\n{block}\n\n{after}"
    else:
        content = f"{content.rstrip()}\n\n{block}\n"

    readme_path.write_text(content.rstrip() + "\n", encoding="utf-8")


def print_today(data: dict) -> None:
    latest = latest_word(data)
    if latest is None:
        print("No words found. Run: python src/word_generator.py init")
        return

    print(f"Word: {latest['word']}")
    print(f"Part of speech: {latest['part_of_speech']}")
    print(f"Difficulty: {latest['difficulty']}")
    print(f"Meaning: {latest['definition']}")
    print(f"Example: {latest['example']}")
    print(f"Added: {latest['date_added']}")


def print_stats(data: dict) -> None:
    words = data.get("words", [])
    by_difficulty: dict[str, int] = {}
    for item in words:
        by_difficulty[item["difficulty"]] = by_difficulty.get(item["difficulty"], 0) + 1

    print(f"Total words: {len(words)}")
    for difficulty in sorted(by_difficulty):
        print(f"{difficulty.title()}: {by_difficulty[difficulty]}")


def print_word_list(data: dict, limit: int) -> None:
    words = data.get("words", [])
    for item in words[-limit:]:
        print(f"{item['date_added']} - {item['word']} ({item['part_of_speech']}): {item['definition']}")


def run_quiz(data: dict, questions: int = 5) -> int:
    words = data.get("words", [])
    if len(words) < 4:
        print("Need at least 4 words to run quiz mode.")
        return 1

    rng = random.SystemRandom()
    selected = rng.sample(words, min(questions, len(words)))
    score = 0

    for index, correct in enumerate(selected, start=1):
        distractors = [item for item in words if item["word"] != correct["word"]]
        options = rng.sample(distractors, min(3, len(distractors))) + [correct]
        rng.shuffle(options)

        print(f"\nQuestion {index}: Which word means '{correct['definition']}'?")
        for option_index, option in enumerate(options, start=1):
            print(f"  {option_index}. {option['word']}")

        answer = input("Your answer: ").strip()
        try:
            choice = int(answer)
        except ValueError:
            choice = -1

        if 1 <= choice <= len(options) and options[choice - 1]["word"] == correct["word"]:
            print("Correct.")
            score += 1
        else:
            print(f"Not quite. The answer is {correct['word']}.")
            print(f"Example: {correct['example']}")

    print(f"\nScore: {score}/{len(selected)}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Daily English word generator with quiz mode.")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA_PATH, help="Path to the JSON word file.")

    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Create the first random word list.")
    init_parser.add_argument("--count", type=int, default=100, help="Number of initial words.")
    init_parser.add_argument("--seed", default=None, help="Optional seed for repeatable random selection.")
    init_parser.add_argument("--overwrite", action="store_true", help="Replace an existing data file.")
    init_parser.add_argument("--readme", action="store_true", help="Update README stats after initializing.")

    add_parser = subparsers.add_parser("add", help="Add one unused daily word.")
    add_parser.add_argument("--seed", default=None, help="Optional seed for repeatable selection.")
    add_parser.add_argument("--timezone", default=DEFAULT_TIMEZONE, help="Local timezone for daily scheduling.")
    add_parser.add_argument("--require-local-hour", type=int, default=None, help="Only add when local hour matches.")
    add_parser.add_argument("--readme", action="store_true", help="Update README stats after adding.")

    subparsers.add_parser("today", help="Print the latest word.")

    quiz_parser = subparsers.add_parser("quiz", help="Start an interactive multiple-choice quiz.")
    quiz_parser.add_argument("--questions", type=int, default=5, help="Number of quiz questions.")

    subparsers.add_parser("stats", help="Show word count and difficulty breakdown.")

    list_parser = subparsers.add_parser("list", help="Print recently added words.")
    list_parser.add_argument("--limit", type=int, default=20, help="Number of words to show.")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "init":
            data = initialize_words(args.count, args.data, args.seed, args.overwrite)
            if args.readme:
                update_readme(data)
            print(f"Created {len(data['words'])} words at {args.data}.")
            return 0

        if args.command == "add":
            changed, message, data = add_daily_word(
                path=args.data,
                timezone_name=args.timezone,
                require_local_hour=args.require_local_hour,
                seed=args.seed,
            )
            if changed and args.readme:
                update_readme(data)
            print(message)
            return 0

        data = load_data(args.data)

        if args.command == "today":
            print_today(data)
            return 0

        if args.command == "quiz":
            return run_quiz(data, args.questions)

        if args.command == "stats":
            print_stats(data)
            return 0

        if args.command == "list":
            print_word_list(data, args.limit)
            return 0

    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
