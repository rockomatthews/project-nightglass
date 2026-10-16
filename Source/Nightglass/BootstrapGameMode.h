#pragma once
#include "CoreMinimal.h"
#include "GameFramework/GameModeBase.h"
#include "BootstrapGameMode.generated.h"

/** M0 connection harness only. No teams, match rules, money or settlement. */
UCLASS()
class NIGHTGLASS_API ABootstrapGameMode : public AGameModeBase
{
    GENERATED_BODY()
public:
    ABootstrapGameMode();
    virtual void PostLogin(APlayerController* NewPlayer) override;
    virtual void Logout(AController* Exiting) override;
};
