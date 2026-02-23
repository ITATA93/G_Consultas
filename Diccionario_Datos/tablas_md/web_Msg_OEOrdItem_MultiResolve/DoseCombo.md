# web_Msg_OEOrdItem_MultiResolve.DoseCombo

**Schema:** web_Msg_OEOrdItem_MultiResolve
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ComboSelected | varchar |  |  | SI | - |
| FewestBUOM | varchar |  |  | NO | - |
| ID | varchar |  |  | NO | - |
| NotCalculated | varchar |  |  | SI | if the CalculateCombosForDose method is not able t... |
| ParRef | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| UserCombo | varchar |  |  | NO | This Combo will be the one that we display for the... |
| UserComboLinkedDR | varchar |  | FK | SI | Onload the UserCombo row will be linked to the Few... |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*