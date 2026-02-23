# SQLUser.RB_ApptSMR00

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SMR00_ParRef | varchar | PK |  | NO | RB_Appointment Parent Reference |
| SMR00_CPMain_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| SMR00_CPOther1_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| SMR00_CPOther2_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| SMR00_CPOther3_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| SMR00_Childsub | double |  |  | NO | Childsub |
| SMR00_Date | date |  |  | SI | Date |
| SMR00_ISDRef | varchar |  |  | SI | ISDRef |
| SMR00_RowId | varchar |  |  | NO | - |
| SMR00_SPPPMainS_DR | bigint |  | FK | SI | Des Ref State PPP |
| SMR00_SPPPMain_DR | bigint |  | FK | SI | Des Ref State PPP |
| SMR00_SPPPOther1S_DR | bigint |  | FK | SI | Des Ref State PPP |
| SMR00_SPPPOther1_DR | bigint |  | FK | SI | Des Ref State PPP |
| SMR00_SPPPOther2S_DR | bigint |  | FK | SI | Des Ref State PPP |
| SMR00_SPPPOther2_DR | bigint |  | FK | SI | Des Ref State PPP |
| SMR00_SPPPOther3S_DR | bigint |  | FK | SI | Des Ref State PPP |
| SMR00_SPPPOther3_DR | bigint |  | FK | SI | Des Ref State PPP |
| SMR00_SubmissionStatus | varchar |  |  | SI | SubmissionStatus |
| SMR00_ValidationStatus | varchar |  |  | SI | ValidationStatus |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*