# questionnaire.QCLXXPA3QQ07

> Plan de acompañamiento alto riesgo hospitalización para adultos mayores con neumonía : Sesiones

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Plan de acompañamiento alto riesgo hospitalización para adultos mayores con neumonía : Sesiones

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q07Q1 | date |  |  | SI | Fecha |
| Q07Q2 | varchar |  |  | SI | Sesión |
| Q07Q3 | varchar |  |  | SI | Temas abordados |
| Q07Q4 | varchar |  |  | SI | Acude con acompañante |
| Q07Q5 | varchar |  |  | SI | Observaciones |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*