#include "BootstrapGameMode.h"
#include "GameFramework/DefaultPawn.h"
#include "GameFramework/PlayerController.h"

DEFINE_LOG_CATEGORY_STATIC(LogNightglassBootstrap, Log, All);

ABootstrapGameMode::ABootstrapGameMode()
{
    DefaultPawnClass = ADefaultPawn::StaticClass();
}

void ABootstrapGameMode::PostLogin(APlayerController* NewPlayer)
{
    Super::PostLogin(NewPlayer);
    UE_LOG(LogNightglassBootstrap, Display, TEXT("M0 client connected; players=%d"), GetNumPlayers());
}

void ABootstrapGameMode::Logout(AController* Exiting)
{
    Super::Logout(Exiting);
    UE_LOG(LogNightglassBootstrap, Display, TEXT("M0 client disconnected"));
}
