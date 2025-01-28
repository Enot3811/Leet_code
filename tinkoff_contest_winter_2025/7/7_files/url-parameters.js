// eslint-disable-next-line import/no-unresolved,import/extensions
import config from './configs/config.js';

function gerParams(search) {
    // TODO: app, auth - для обратной совместимости со старым launcher-ом, убрать после релиза в TMSG-20899
    const {app, auth, appId, authSystem, authZone} = Object.fromEntries(
        new URLSearchParams(search),
    );

    return {
        appId: appId || app,
        authSystem: authSystem || auth,
        authZone,
    };
}

const queryParams = gerParams(document.location.search);

function setParams({appId, authSystem, authZone}) {
    config.appId = appId;
    config.authSystem = authSystem;
    config.authZone = authZone;
}

if (queryParams.appId) {
    setParams(queryParams);
} else {
    window.addEventListener(`message`, function listener(event) {
        if (!event.data) {
            return;
        }

        if (event.data.messageCode === `tmsg-url-response`) {
            const params = gerParams(new URL(event.data.data).search);

            if (params.appId) {
                setParams(params);
            }

            window.removeEventListener(`message`, listener);
        }
    });

    window.parent.postMessage(
        {
            messageCode: `tmsg-url-request`,
        },
        `*`,
    );
}
