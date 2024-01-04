namespace PMTester.Services;

public class HttpClient : IHttpClient
{
    private System.Net.Http.HttpClient _client;
    private string _baseUrl = "██████████";

    public HttpClient() {
        _client = new System.Net.Http.HttpClient();
    }

    public void ClearHeaders() {
        _client.DefaultRequestHeaders.Clear();
    }

    public void AddHeader(string name, string value) {
        _client.DefaultRequestHeaders.Add(name, value);
    }

    public async Task<HttpResponseMessage> Get(string requestUri)
    {
        var res = await _client.GetAsync(_baseUrl + requestUri);
        return res;
    }

    public async Task<HttpResponseMessage> Post(string requestUri, HttpContent? content)
    {
        var res = await _client.PostAsync(_baseUrl + requestUri, content);
        return res;
    }
}