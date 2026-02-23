# web_Msg_LBTransfer_Combined.Edit

**Schema:** web_Msg_LBTransfer_Combined
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ExclusionListLabSite | varchar |  |  | SI | A list of Lab Sites to exclude in the To Lab Site ... |
| ExclusionListRefLab | varchar |  |  | SI | A list of Referral Labs to exclude in the To Refer... |
| FromLabSiteDR | bigint |  | FK | SI | The current From Lab Site common to all the select... |
| ID | varchar |  |  | NO | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| SpecimenCount | integer |  |  | SI | A count of all the specimens selected |
| ToLabSiteDR | bigint |  | FK | SI | The current To Lab Site common to all the selected... |
| ToReferralLabDR | bigint |  | FK | SI | The current To Referral Lab common to all the sele... |
| TransferCount | integer |  |  | SI | A count of all the transfers selected |
| TransferList | varchar |  |  | SI | A list of LBTransferID representing all the transf... |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*