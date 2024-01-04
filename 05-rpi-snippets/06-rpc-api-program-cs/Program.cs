using PMTester.Services;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Log path
string logPath = string.Empty;
if (OperatingSystem.IsLinux()) {
    logPath = Path.Join(Environment.GetFolderPath(Environment.SpecialFolder.UserProfile), ".local", "logs", "pmtester");
}
else if (OperatingSystem.IsWindows()) {
    logPath = Path.Join(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "pmtester", "logs");
}


// DI
builder.Services.AddSingleton<PMTester.Services.ILogger, Logger>(_ => new Logger(logPath));
builder.Services.AddSingleton<IHttpClient, PMTester.Services.HttpClient>();

// Set urls
#if DEBUG
builder.WebHost.UseUrls("http://*:5000", "https://*:5001");
#elif RELEASE
builder.WebHost.UseUrls("http://*:5000", "https://*:5001");
#endif

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();
