# SQLUser.PAC_QuestionRespAnsCont

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESCONT_ParRef | varchar | PK |  | NO | SS_UserDefWinContResp Parent Reference |
| Q09Q1 | - |  |  | SI | Specify site	 |
| Q09Q2 | - |  |  | SI | Lot number	 |
| Q09Q3 | - |  |  | SI | Expiry date	 |
| Q09Q4 | - |  |  | SI | Monopolar |
| Q09Q5 | - |  |  | SI | Bipolar |
| Q09Q6 | - |  |  | SI | Has the diathermy site been shaved? |
| QUESCONT_Childsub | double |  |  | NO | Childsub |
| QUESCONT_Ques_DR | bigint |  | FK | SI | Des Ref PACQuestion |
| QUESCONT_RowId | varchar |  |  | NO | - |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*