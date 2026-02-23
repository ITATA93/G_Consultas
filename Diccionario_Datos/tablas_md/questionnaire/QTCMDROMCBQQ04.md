# questionnaire.QTCMDROMCBQQ04

> Multidrug Resistant Organism Maintenance Care Bundle : Multidrug resistant organism bundle

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Multidrug Resistant Organism Maintenance Care Bundle : Multidrug resistant organism bundle

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q04Q1 | numeric |  |  | SI | Day |
| Q04Q10 | time |  |  | SI | Assessment time |
| Q04Q2 | varchar |  |  | SI | The antibiotic is prescribed in accordance with ho... |
| Q04Q3 | varchar |  |  | SI | Culture and sensitivity result is reviewed. |
| Q04Q4 | varchar |  |  | SI | Contact precaution is implemented and proper used ... |
| Q04Q5 | varchar |  |  | SI | Environmental cleaning using hospital approved dis... |
| Q04Q6 | varchar |  |  | SI | Hand hygiene |
| Q04Q7 | varchar |  |  | SI | Decolonization |
| Q04Q8 | varchar |  |  | SI | Assessing care provider |
| Q04Q9 | date |  |  | SI | Assessment date |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*