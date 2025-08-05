from transformers import pipeline

classifier = pipeline("text-classification", model="Giyaseddin/distilbert-base-cased-finetuned-fake-and-real-news-dataset", top_k=None)
# examples = ["Obama is running for president in 2016"]

var = input("Please enter news text want to verify: ")
result = classifier(var)

# map generic labels to readable
label_mapping = {
    'LABEL_0': 'REAL',
    'LABEL_1': 'FAKE'
}
# convert results to readable format
for i, example_result in enumerate(result):
    print(f"Text {i+1} Analysis: ")
    print("-" * 30)

    for prediction in example_result:
        readable_label = label_mapping.get(prediction['label'], prediction['label'])
        confidence = prediction['score'] * 100
        print(f"{readable_label}: {confidence:.2f}%")

    top_prediction = max(example_result, key=lambda x: x['score'])
    final_label = label_mapping.get(top_prediction['label'],top_prediction['label'])
    print(f"\nVerdict: This news appears to be '{final_label}'")
    print("=" * 40)