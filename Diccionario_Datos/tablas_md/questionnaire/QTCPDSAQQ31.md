# questionnaire.QTCPDSAQQ31

> Peritoneal Dialysis Suitability Assessment : Dexterity

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peritoneal Dialysis Suitability Assessment : Dexterity

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q31Q1 | varchar |  |  | SI | Dexterity assessment for |
| Q31Q2 | varchar |  |  | SI | Able to attend to peritoneal dialysis connection |
| Q31Q3 | varchar |  |  | SI | Able to attend to peritoneal dialysis disconnectio... |
| Q31Q4 | varchar |  |  | SI | Able to open gauze packaging |
| Q31Q5 | varchar |  |  | SI | Able to clamp  unclamp catheter lines |
| Q31Q6 | varchar |  |  | SI | Able to remove and replace cap |
| Q31Q7 | varchar |  |  | SI | Able to break phalange |
| Q31Q8 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*