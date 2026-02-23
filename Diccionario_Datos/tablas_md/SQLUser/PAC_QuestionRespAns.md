# SQLUser.PAC_QuestionRespAns

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESRA_ParRef | bigint | PK |  | NO | PAC_Question Parent Reference |
| QUESRA_Childsub | double |  |  | NO | Childsub |
| QUESRA_Code | varchar |  |  | SI | Code |
| QUESRA_DateFrom | date |  |  | SI | DateFrom |
| QUESRA_DateTo | date |  |  | SI | DateTo |
| QUESRA_Desc | varchar |  |  | SI | Description |
| QUESRA_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*