from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insertintotable', methods=['POST'])
def insertintotable():
    # Get the stock symbol from the form
    nm = request.form['nm']
    
    # Here you would add your logic to get stock data and perform predictions
    # Then redirect to results page with the data
    # For now, we'll just redirect to a placeholder
    
    # If stock not found
    # return render_template('index.html', not_found=True)
    
    # If stock found, return results page with data
    # Sample data - replace with actual data processing
    return render_template('results.html', 
                          quote=nm, 
                          open_s="100.00", 
                          high_s="105.00", 
                          low_s="98.00", 
                          close_s="103.00",
                          adj_close="103.00",
                          vol="1000000",
                          arima_pred="105.20",
                          lstm_pred="104.80",
                          lr_pred="104.50",
                          error_arima="0.5",
                          error_lstm="0.4",
                          error_lr="0.6",
                          tw_list=["Sample tweet 1", "Sample tweet 2"] * 6,
                          tw_pol="0.65",
                          idea="rise",
                          decision="BUY",
                          forecast_set=[[104.50], [105.20], [106.10], [106.80], [107.50], [108.20], [109.00]])

if __name__ == '__main__':
    app.run(debug=True)