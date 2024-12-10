test_json_response = {
    "criteria": {
        "Task Achievement": {
            "description": "Does the response fulfill the requirements of the task? Does it clearly summarize and highlight the key features, trends, or comparisons in the visual data? Is it accurate and sufficiently detailed without including irrelevant information?",
            "band_range": "1-9",
        },
        "Coherence and Cohesion": {
            "description": "Is the information logically organized and linked? Are cohesive devices (e.g., linking words, pronouns) used effectively and appropriately? Is the overall flow natural?",
            "band_range": "1-9",
        },
        "Lexical Resource": {
            "description": "Does the response use a range of vocabulary effectively? Are words and phrases varied and appropriate for the task? Are there any issues with spelling or word choice?",
            "band_range": "1-9",
        },
        "Grammatical Range and Accuracy": {
            "description": "Is a variety of sentence structures used effectively? Are there errors in grammar, punctuation, or sentence formation? How accurate and complex is the language?",
            "band_range": "1-9",
        },
    },
    "output_format": {
        "feedback": {
            "Task Achievement": "Provide detailed comments and justification for the band score.",
            "Coherence and Cohesion": "Provide detailed comments and justification for the band score.",
            "Lexical Resource": "Provide detailed comments and justification for the band score.",
            "Grammatical Range and Accuracy": "Provide detailed comments and justification for the band score.",
        },
        "overall_band_score": "Provide an overall band score (1-9) as an average of the four criteria.",
        "improvement_suggestions": "Give specific advice on how to improve the response across all criteria.",
    },
    'words': {
        'old word': 'best alternative',
    }
}

task1_assesment = {
  "BandDescriptors": [
    {
      "Band": 9,
      "TaskAchievement": "Fully satisfies all the requirements of the task. Clearly presents a fully developed response.",
      "CoherenceAndCohesion": "Uses cohesion in such a way that it attracts no attention. Skillfully manages paragraphing.",
      "LexicalResource": "Uses a wide range of vocabulary with very natural and sophisticated control of lexical features. Rare minor errors occur as 'slips.'",
      "GrammaticalRangeAndAccuracy": "Uses a wide range of structures with full flexibility and accuracy. Rare minor errors occur."
    },
    {
      "Band": 8,
      "TaskAchievement": "Covers all requirements of the task sufficiently. Presents, highlights, and illustrates key features/bullet points clearly and appropriately.",
      "CoherenceAndCohesion": "Sequences information and ideas logically. Manages all aspects of cohesion well. Uses paragraphing sufficiently and appropriately.",
      "LexicalResource": "Uses a wide range of vocabulary fluently and flexibly to convey precise meanings. Skillfully uses uncommon lexical items but may produce occasional inaccuracies in word choice and collocation. Rare errors in spelling and/or word formation.",
      "GrammaticalRangeAndAccuracy": "Uses a wide range of structures. The majority of sentences are error-free. Makes very occasional errors or inappropriacies."
    },
    {
      "Band": 7,
      "TaskAchievement": "Covers the requirements of the task. Presents a clear overview of main trends, differences, or stages. Clearly presents and highlights key features/bullet points but could be more fully extended.",
      "CoherenceAndCohesion": "Logically organizes information and ideas; there is clear progression throughout. Uses a range of cohesive devices appropriately, although there may be some under-/over-use.",
      "LexicalResource": "Uses a sufficient range of vocabulary to allow some flexibility and precision. Uses less common lexical items with some awareness of style and collocation. Produces occasional errors in word choice, spelling, and/or word formation.",
      "GrammaticalRangeAndAccuracy": "Uses a variety of complex structures. Produces frequent error-free sentences. Has good control of grammar and punctuation but may make a few errors."
    },
    {
      "Band": 6,
      "TaskAchievement": "Addresses the requirements of the task. Presents an overview with information appropriately selected. Presents and adequately highlights key features, but details may be irrelevant, inappropriate, or inaccurate.",
      "CoherenceAndCohesion": "Arranges information and ideas coherently, and there is a clear overall progression. Uses cohesive devices effectively, but cohesion within and/or between sentences may be faulty or mechanical. May not always use referencing clearly or appropriately.",
      "LexicalResource": "Uses an adequate range of vocabulary for the task. Attempts to use less common vocabulary but with some inaccuracy. Makes some errors in spelling and/or word formation, but they do not impede communication.",
      "GrammaticalRangeAndAccuracy": "Uses a mix of simple and complex sentence forms. Makes some errors in grammar and punctuation, but they rarely reduce communication."
    },
    {
      "Band": 5,
      "TaskAchievement": "Generally addresses the task; the format may be inappropriate in places. Recounts detail mechanically with no clear overview; there may be no data to support the description. Presents, but inadequately covers, key features/bullet points; there may be a tendency to focus on details.",
      "CoherenceAndCohesion": "Presents information with some organization, but there may be a lack of overall progression. Makes inadequate, inaccurate, or over-use of cohesive devices. May be repetitive because of lack of referencing and substitution.",
      "LexicalResource": "Uses a limited range of vocabulary, but this is minimally adequate for the task. May make noticeable errors in spelling and/or word formation that may cause some difficulty for the reader.",
      "GrammaticalRangeAndAccuracy": "Uses only a limited range of structures. Attempts complex sentences but these tend to be less accurate than simple sentences. May make frequent grammatical errors and punctuation may be faulty; errors can cause some difficulty for the reader."
    },
    {
      "Band": 4,
      "TaskAchievement": "Attempts to address the task but does not cover all key features/bullet points; the format may be inappropriate. May confuse key features/bullet points with detail; parts may be unclear, irrelevant, repetitive, or inaccurate.",
      "CoherenceAndCohesion": "Presents information and ideas, but they are not arranged coherently, and there is no clear progression. Uses some basic cohesive devices, but these may be inaccurate or repetitive.",
      "LexicalResource": "Uses only basic vocabulary, which may be used repetitively or which may be inappropriate for the task. Has limited control of word formation and/or spelling; errors may cause strain for the reader.",
      "GrammaticalRangeAndAccuracy": "Uses only a very limited range of structures, with only rare use of subordinate clauses. Some structures are accurate, but errors predominate, and punctuation is often faulty."
    },
    {
      "Band": 3,
      "TaskAchievement": "Fails to address the task, which may be completely misunderstood. Presents limited ideas that may be largely irrelevant/repetitive.",
      "CoherenceAndCohesion": "Does not organize ideas logically. May use a very limited range of cohesive devices, and those used may not indicate a logical relationship between ideas.",
      "LexicalResource": "Uses only a very limited range of words and expressions. Errors may severely distort the message.",
      "GrammaticalRangeAndAccuracy": "Attempts sentence forms, but errors in grammar and punctuation predominate and distort the meaning."
    },
    {
      "Band": 2,
      "TaskAchievement": "Answer is barely related to the task.",
      "CoherenceAndCohesion": "Has very little control of organizational features.",
      "LexicalResource": "Uses an extremely limited range of vocabulary; essentially no control of word formation and/or spelling.",
      "GrammaticalRangeAndAccuracy": "Cannot use sentence forms except in memorized phrases."
    },
    {
      "Band": 1,
      "TaskAchievement": "Answer is completely unrelated to the task.",
      "CoherenceAndCohesion": "Fails to communicate any message.",
      "LexicalResource": "Can only use a few isolated words.",
      "GrammaticalRangeAndAccuracy": "Cannot use sentence forms at all."
    },
    {
      "Band": 0,
      "TaskAchievement": "No response or does not attempt the task in any way. Writes a totally memorized response."
    }
  ]
}


task2_assesment = {
  "BandDescriptors": [
    {
      "Band": 9,
      "TaskResponse": "Fully addresses all parts of the task. Presents a fully developed position in answer to the question with relevant, fully extended, and well-supported ideas.",
      "CoherenceAndCohesion": "Uses cohesion in such a way that it attracts no attention. Skillfully manages paragraphing.",
      "LexicalResource": "Uses a wide range of vocabulary with very natural and sophisticated control of lexical features. Rare minor errors occur only as 'slips.'",
      "GrammaticalRangeAndAccuracy": "Uses a wide range of structures with full flexibility and accuracy. Rare minor errors occur only as 'slips.'"
    },
    {
      "Band": 8,
      "TaskResponse": "Sufficiently addresses all parts of the task. Presents a well-developed response to the question with relevant, extended, and supported ideas.",
      "CoherenceAndCohesion": "Sequences information and ideas logically. Manages all aspects of cohesion well. Uses paragraphing sufficiently and appropriately.",
      "LexicalResource": "Uses a wide range of vocabulary fluently and flexibly to convey precise meanings. Skillfully uses uncommon lexical items but there may be occasional inaccuracies in word choice and collocation. Produces rare errors in spelling and/or word formation.",
      "GrammaticalRangeAndAccuracy": "Uses a wide range of structures. The majority of sentences are error-free. Makes only very occasional errors or inappropriacies."
    },
    {
      "Band": 7,
      "TaskResponse": "Addresses all parts of the task. Presents a clear position throughout the response. Presents, extends, and supports main ideas, but there may be a tendency to overgeneralize and/or supporting ideas may lack focus.",
      "CoherenceAndCohesion": "Logically organizes information and ideas; there is clear progression throughout. Uses a range of cohesive devices appropriately, although there may be some under-/over-use. Presents a clear central topic within each paragraph.",
      "LexicalResource": "Uses a sufficient range of vocabulary to allow some flexibility and precision. Uses less common lexical items with some awareness of style and collocation. Produces occasional errors in word choice, spelling, and/or word formation.",
      "GrammaticalRangeAndAccuracy": "Uses a variety of complex structures. Produces frequent error-free sentences. Has good control of grammar and punctuation but may make a few errors."
    },
    {
      "Band": 6,
      "TaskResponse": "Addresses all parts of the task, although some parts may be more fully covered than others. Presents a relevant position, although the conclusions may become unclear or repetitive. Presents relevant main ideas, but some may be inadequately developed or unclear.",
      "CoherenceAndCohesion": "Arranges information and ideas coherently, and there is a clear overall progression. Uses cohesive devices effectively, but cohesion within and/or between sentences may be faulty or mechanical. May not always use referencing clearly or appropriately. Uses paragraphing, but not always logically.",
      "LexicalResource": "Uses an adequate range of vocabulary for the task. Attempts to use less common vocabulary but with some inaccuracy. Makes some errors in spelling and/or word formation, but they do not impede communication.",
      "GrammaticalRangeAndAccuracy": "Uses a mix of simple and complex sentence forms. Makes some errors in grammar and punctuation, but they rarely reduce communication."
    },
    {
      "Band": 5,
      "TaskResponse": "Addresses the task only partially; the format may be inappropriate in places. Expresses a position, but the development is not always clear and there may be no conclusions drawn. Presents some main ideas but these are limited and not sufficiently developed; there may be irrelevant detail.",
      "CoherenceAndCohesion": "Presents information with some organization, but there may be a lack of overall progression. Makes inadequate, inaccurate, or over-use of cohesive devices. May be repetitive because of lack of referencing and substitution. May not write in paragraphs, or paragraphs may be inadequate.",
      "LexicalResource": "Uses a limited range of vocabulary, but this is minimally adequate for the task. May make noticeable errors in spelling and/or word formation that may cause some difficulty for the reader.",
      "GrammaticalRangeAndAccuracy": "Uses only a limited range of structures. Attempts complex sentences but these tend to be less accurate than simple sentences. May make frequent grammatical errors and punctuation may be faulty; errors can cause some difficulty for the reader."
    },
    {
      "Band": 4,
      "TaskResponse": "Responds to the task only in a minimal way or the answer is tangential; the format may be inappropriate. Presents a position, but this is unclear. Presents some main ideas but these are difficult to identify and may be repetitive, irrelevant, or not well supported.",
      "CoherenceAndCohesion": "Presents information and ideas, but they are not arranged coherently, and there is no clear progression. Uses some basic cohesive devices, but these may be inaccurate or repetitive. May not write in paragraphs or their use may be confusing.",
      "LexicalResource": "Uses only basic vocabulary, which may be used repetitively or which may be inappropriate for the task. Has limited control of word formation and/or spelling; errors may cause strain for the reader.",
      "GrammaticalRangeAndAccuracy": "Uses only a very limited range of structures with only rare use of subordinate clauses. Some structures are accurate, but errors predominate, and punctuation is often faulty."
    },
    {
      "Band": 3,
      "TaskResponse": "Does not adequately address any part of the task. Does not express a clear position. Presents few ideas, which are largely undeveloped or irrelevant.",
      "CoherenceAndCohesion": "Does not organize ideas logically. May use a very limited range of cohesive devices, and those used may not indicate a logical relationship between ideas.",
      "LexicalResource": "Uses only a very limited range of words and expressions. Errors may severely distort the message.",
      "GrammaticalRangeAndAccuracy": "Attempts sentence forms, but errors in grammar and punctuation predominate and distort the meaning."
    },
    {
      "Band": 2,
      "TaskResponse": "Barely responds to the task. Does not express a position. May attempt to present one or two ideas, but there is no development.",
      "CoherenceAndCohesion": "Has very little control of organizational features.",
      "LexicalResource": "Uses an extremely limited range of vocabulary; essentially no control of word formation and/or spelling.",
      "GrammaticalRangeAndAccuracy": "Cannot use sentence forms except in memorized phrases."
    },
    {
      "Band": 1,
      "TaskResponse": "Answer is completely unrelated to the task.",
      "CoherenceAndCohesion": "Fails to communicate any message.",
      "LexicalResource": "Can only use a few isolated words.",
      "GrammaticalRangeAndAccuracy": "Cannot use sentence forms at all."
    },
    {
      "Band": 0,
      "TaskResponse": "Does not attend. Does not attempt the task in any way. Writes a totally memorized response."
    }
  ]
}



Task1_prompt = f""" You are an expert in assessing IELTS Writing Task 1 responses. Evaluate the given response based on the following json: {task1_assesment} Also, suggest specific improvements.
Just keep in mind that the detailed feedback and explanation should be less that 200 words. You should tell the main idea within that limit. By the way, ignore this letters: '\n' or '\t' in the response. Do not strictly assess the essay as beginners and intermediate level students try to use your experience and knowledge to help them improve.
If text is in another language,except english, just ignore and return 'None' word! Also, if other things like html code or js code or any codes as a whole, dont accept them, And return 'Incorrect text' 
Response should be like json and in this format:
{test_json_response}
inside of json, please tell  must-to-change words which are lowering the score and suggest alternatives to them. This should be like: 
must-change-words: an alternative of that words that suits the content
"""

Task2_prompt = f""" You are an expert in assessing IELTS Writing Task 2 responses. Evaluate the given response based on the following json: {task2_assesment} Also, suggest specific improvements.
Just keep in mind that the detailed feedback and explanation should be less that 200 words. You should tell the main idea within that limit. By the way, ignore this letters: '\n' or '\t' in the response. Do not strictly assess the essay as beginners and intermediate level students try to use your experience and knowledge to help them improve.
If text is in another language, except for english, just ignore and return 'None' word! Also, if other things like html code or js code or any codes as a whole, dont accept them, then return 'Incorrect text'. return 'Incorrect text' when not text but some kind of programming language codes are inserted, only in this case.
Response should be like json and in this format:
{test_json_response}
inside of json, please tell must-to-change words which are lowering the score and suggest alternatives to them. This should be like: 
must-change-words: an alternative of that words that suits the content
"""


