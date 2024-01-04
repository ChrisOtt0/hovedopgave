namespace PMTester.Services;

public interface IHttpClient {
    public void ClearHeaders();
    
    public void AddHeader(string name, string value);

    public Task<HttpResponseMessage> Get(string requestUri);

    public Task<HttpResponseMessage> Post(string requestUri, HttpContent? content);
}