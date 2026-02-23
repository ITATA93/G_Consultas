# questionnaire.QCLXXMDIQQ10

> Mantención Dispositivos Invasivos : Drenajes

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Mantención Dispositivos Invasivos : Drenajes

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q10Q1 | varchar |  |  | SI | Tipo Drenajes |
| Q10Q10 | varchar |  |  | SI | ¿Es Necesario el DI? |
| Q10Q2 | varchar |  |  | SI | Subtipo |
| Q10Q3 | varchar |  |  | SI | Tamaño |
| Q10Q4 | varchar |  |  | SI | Actividad |
| Q10Q5 | varchar |  |  | SI | Ubicación |
| Q10Q6 | varchar |  |  | SI | Zona Inserción |
| Q10Q7 | varchar |  |  | SI | Descripción del Contenido |
| Q10Q8 | varchar |  |  | SI | Estado de la Cobertura |
| Q10Q9 | varchar |  |  | SI | N° Días de Drenaje |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*