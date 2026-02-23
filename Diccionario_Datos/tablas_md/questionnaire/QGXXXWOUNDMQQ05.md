# questionnaire.QGXXXWOUNDMQQ05

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | varchar | PK |  | NO | - |
| Q05Q1 | date | PK |  | SI | Date |
| Q05Q10 | varchar | PK |  | SI | Skin colour surrounding wound |
| Q05Q11 | varchar | PK |  | SI | Granulation tissue |
| Q05Q15 | varchar | PK |  | SI | Note |
| Q05Q2 | varchar | PK |  | SI | Size right/left // top/down (mm) |
| Q05Q3 | varchar | PK |  | SI | Depth |
| Q05Q4 | varchar | PK |  | SI | Edges |
| Q05Q5 | varchar | PK |  | SI | Undermining |
| Q05Q6 | varchar | PK |  | SI | Excudate |
| Q05Q6a | varchar | PK |  | SI | Wound infection |
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| childsub | bigint | PK |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*