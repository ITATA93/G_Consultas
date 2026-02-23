# web_Msg.LB_ResultDeltaCheck

**Schema:** web_Msg
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Resultados de Laboratorio**. Valores de exámenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| DownAbsoluteValue | double |  |  | SI | Absolute Value Decrease |
| DownDeltaCheckDR | varchar |  | FK | SI | Delta Check used for Decreases |
| DownInterpretationDR | bigint |  | FK | SI | Clinical Interpretation for Increases
Applied whe... |
| DownPercentage | double |  |  | SI | Percentage Value Decrease |
| DownRateOfChange | double |  |  | SI | Rate of Change for Decreases |
| DownRateOfChangeUnit | varchar |  |  | SI | Rate of Change Unit for Decreases |
| ID | varchar |  |  | NO | - |
| LastResultInterval | varchar |  |  | SI | Interval to previous result |
| LastTestSetItemDR | varchar |  | FK | SI | Previous Test Set Item |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| TextChange | varchar |  |  | SI | Text Change |
| TextDeltaCheckDR | varchar |  | FK | SI | Delta Check used for Text Changes |
| TextInterpretationDR | bigint |  | FK | SI | Clinical Interpretation for Text Change
Applied w... |
| UpAbsoluteValue | double |  |  | SI | Absolute Value Increase |
| UpDeltaCheckDR | varchar |  | FK | SI | Delta Check used for Increases |
| UpInterpretationDR | bigint |  | FK | SI | Clinical Interpretation for Increases
Applied whe... |
| UpPercentage | double |  |  | SI | Percentage Value Increase |
| UpRateOfChange | double |  |  | SI | Rate of Change for Increases |
| UpRateOfChangeUnit | varchar |  |  | SI | Rate of Change Unit for Increases |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*