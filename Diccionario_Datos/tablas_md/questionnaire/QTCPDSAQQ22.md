# questionnaire.QTCPDSAQQ22

> Peritoneal Dialysis Suitability Assessment : Skin conditions

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peritoneal Dialysis Suitability Assessment : Skin conditions

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q22Q1 | varchar |  |  | SI | Skin condition assessment for |
| Q22Q2 | varchar |  |  | SI | Lesions |
| Q22Q3 | varchar |  |  | SI | Infections |
| Q22Q4 | varchar |  |  | SI | Rashes |
| Q22Q5 | varchar |  |  | SI | Fungal |
| Q22Q6 | varchar |  |  | SI | Skin scrapings |
| Q22Q7 | varchar |  |  | SI | Chronic open wounds or skin conditions |
| Q22Q8 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*