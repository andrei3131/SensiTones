require 'net/http'

request_text = ""

file = File.new("reqbuffer.txt", "r")
while (line = file.gets)
    request_text << line
end
file.close

uri = URI('https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment')
uri.query = URI.encode_www_form({
})

request = Net::HTTP::Post.new(uri.request_uri)

request['Content-Type'] = 'application/json'
request['Ocp-Apim-Subscription-Key'] = '7911c204a38749acba19d26e6bb2e763'

request.body = '{
  "documents": [
    {
      "language": "en",
      "id": "ruby_req",
      "text": "' << request_text << '"
    }
  ]
}'

response = Net::HTTP.start(uri.host, uri.port, :use_ssl => uri.scheme == 'https') do |http|
    http.request(request)
end

puts response.body
