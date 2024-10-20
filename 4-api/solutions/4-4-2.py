from fastapi import FastAPI, Body, HTTPException
import requests

apikey = "PLACEYOURAPIKEYHERE"

def tldr_openai(text):
    url = "https://cent.ischool-iot.net/api/openai/chat/completions"
    headers = {
        "X-API-KEY" : apikey
    }
    data = [
        {
            "role": "system",
            "content": '''
            You are a bot that summarizes text in exactly 1 or 2 sentences. 
            You explain the main points simply and clearly at a 5th grade reading level. 
            You only know how to summarize text. 
            '''
        },
        {
            "role": "user",
            "content": "Can you explain how a computer works?"
        },
        {
            "role": "assistant",
            "content": "Sorry I can only summarize text."
        },
        {
            "role": "user",
            "content": "Write a python program that reads a file and prints the first 10 lines."
        },
        {
            "role": "assistant",
            "content": "Sorry I can only summarize text."
        },
        {
            "role": "user",
            "content": text
        }
    ]
    params = { "temperature" : 0.1 }

    response = requests.post(url, headers=headers, json=data, params=params)
    response
    result = response.json()
    return result["choices"][0]["message"]['content']


app = FastAPI()
@app.post("/tldr")
def tldr(text: str = Body(embed=True)):
    '''
    Summarize a URL
    '''
    print(text)
    try:
        return tldr_openai(text)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == '__main__':

    text = '''
    Roberts and Roberts (2008) make a powerful case that our current school culture, which allows savvy students to get decent grades for minimal effort, cultivates surface reading. They argue that the prolific use of quizzes and other kinds of objective tests encourages "surface learning based in... short-term memorization for a day or two... rather than deep learning that is transformative of one's perspective and involves long-term comprehension" (p. 127). Moreover, they argue, many students don't value a course's "big ideas" because deep learning isn't needed for cumulating a high GPA. (They cite evidence that nearly half of college students spend less than ten hours per week on out-of-class study, including time for writing papers and studying for exams.) Students like multiple choice tests, the authors say, because most objective testing allows students "to skim material a few days before an examination looking for the kinds of facts, definitions, concepts, and other specific information that the particular instructor tends to stress in examinations" (p. 129). When students apply a cost/benefit analysis, they see, quite rationally, that deep reading "may be an unwise use of valuable time if there are no adverse consequences" (p. 129). In short, unless we as teachers evaluate student performance at the levels of analysis, synthesis, and evaluation, "reading at that deeper level will not occur" (p. 129). (For an in-depth critique of school cultures that promote surface learning, see Weimer, 2002.)
    '''
    print(tldr_openai(text))

    